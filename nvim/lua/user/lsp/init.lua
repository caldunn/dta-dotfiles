local ok, mason = pcall(require, "mason")
if not ok then 
  return 
end 
local ok, _ = pcall(require, "lspconfig")
if not ok then 
  print("LSP Config is not loading")
  return 
end


require('user/lsp/lsp-installer')
mason.setup()
