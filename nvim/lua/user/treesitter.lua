local ok, configs = pcall(require, "nvim-treesitter.configs")
if not ok then return end

configs.setup {
  ensure_installed = "all",
  sync_install = false,
  ignore_install = {""},
  highlight = {
    enable = true,
    disable = {""},
    additional_vim_regex_highlighting = true,
  },
  indent = { enable = true, disable = {"yaml"}},
  -- Rainbow for parens
  rainbow = {
    enable = true,
    extended_mode = true,
    max_file_lines = nil,
    colors = {
      "#E06c75",
      "#E5C07B",
      "#61AFEF",
      "#C678DD",
      "#56B6C2"
    }
  },
}
