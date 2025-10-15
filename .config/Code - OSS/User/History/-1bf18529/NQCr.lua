require("config.lazy")
    return {
      "RedsXDD/neopywal.nvim",
      config = function()
        require("neopywal").setup({
          -- Optional: Configure neopywal settings here
          -- For example, to enable light mode if using wal -l
          -- light_mode = true,
        })
      end,
    }