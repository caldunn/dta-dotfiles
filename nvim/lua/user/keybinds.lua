-- Functional wrapper for mapping custom keybindings
local function map(mode, lhs, rhs, opts)
	local options = { noremap = true }
	if opts then
		options = vim.tbl_extend("force", options, opts)
	end
	vim.keymap.set(mode, lhs, rhs, options)
end

local function mapn(lhs, rhs, opts)
	map("n", lhs, rhs, opts)
end

local function mapi(lhs, rhs, opts)
	map("i", lhs, rhs, opts)
end

local function mapx(lhs, rhs, opts)
	map("x", lhs, rhs, opts)
end

local function mapv(lhs, rhs, opts)
	map("v", lhs, rhs, opts)
end

local bind = vim.api.nvim_set_keymap
local mop = { noremap = true, silent = true }

vim.g.mapleader = " "

-- Fast Reload
mapn("<C-r>", ":luafile %<CR>")

-- double space last file
mapn("<leader><leader>", "<C-^>")
mapn("<leader>rn", "<cmd>lua vim.lsp.buf.rename()<CR>")
-- Visual indenting
mapv(">", ">gv")
mapv("<", "<gv")

-- Move text vertically
mapv("<A-j>", ":m .+1<CR>==")
mapv("<A-k>", ":m .-1<CR>==")

-- Hold the paste
mapv("p", '"_dp')

mapn("<C-h>", "<C-w>h")
mapn("<C-j>", "<C-w>j")
mapn("<C-k>", "<C-w>k")
mapn("<C-l>", "<C-w>l")

mapn("<S-t>", ":tabnew<CR>")
mapn("<S-h>", ":tabnext<CR>")
mapn("<S-l>", ":tabprevious<CR>")
