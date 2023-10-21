local ok, prettier = pcall(require, "prettier")
if not ok then
	return
end

prettier.setup {
  bin = 'prettierd',
  filetypes = {
    'svelte',
  }
}
