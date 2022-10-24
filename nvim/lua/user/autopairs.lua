local ok, npairs = pcall(require, "nvim-autopairs")
if not ok then 
  return
end

npairs.setup {
  check_ts = true,
  disable_filetype = {"TelescopePrompt", "spectre_panel"},
  fast_wrap = {
    map = "<C-l>",
    chars = {"{", "(", "[", "<", '"', "'", "`"},
  },
}
