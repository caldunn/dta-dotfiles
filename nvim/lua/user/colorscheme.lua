local colorscheme = "tokyonight-night"

local ok, _ = pcall(vim.cmd, "colorscheme " .. colorscheme)

if not ok then
	print("Colourscheme failed to load. Are you sure it is installed?")
	return
end
