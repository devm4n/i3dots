    return {
      -- ... other plugins
      {
        "RedsXDD/neopywal.nvim",
        config = function()
          require("neopywal").setup({
            -- Optional: configure neopywal options here
            -- For example, to set a specific theme or enable certain integrations
          })
        end,
      },
      -- ... other plugins
    }