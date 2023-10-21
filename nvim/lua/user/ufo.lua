local ok, ufo = pcall(require, "nvim-ufo")
if not ok then
	return
end
ufo.setup()
