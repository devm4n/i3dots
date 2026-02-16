vim.g.lazyvim_colorscheme = ""
require("config.lazy")
return {
  "RedsXDD/neopywal.nvim",
  config = function()
    require("neopywal").setup({
      -- Optional: Configure neopywal settings here
      -- For example, to enable light mode if using wal -l
      -- light_mode = true,
    })
    --load Pywal Colors
    local wal_colors = os.getenv("HOME") .. "/.cache/wal/colors-wal.vim"
    vim.cmd("source" .. wal_colors)
  end,
}
