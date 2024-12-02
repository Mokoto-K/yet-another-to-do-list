return {
    "VonHeikemen/lsp-zero.nvim",
    branch = "v2.x",
    dependencies = {
        "neovim/nvim-lspconfig",     -- LSP Config
        "williamboman/mason.nvim",   -- Easy installation of LSP servers
        "williamboman/mason-lspconfig.nvim", -- Integrates mason with lspconfig
        "hrsh7th/nvim-cmp",          -- Completion plugin
        "hrsh7th/cmp-nvim-lsp",      -- LSP source for nvim-cmp
        "hrsh7th/cmp-buffer",        -- Buffer completion
        "hrsh7th/cmp-path",          -- Path completion
        "hrsh7th/cmp-cmdline",       -- Cmdline completion
        "L3MON4D3/LuaSnip",          -- Snippet engine for completion
    },
    config = function()
        local lsp = require("lsp-zero")

        -- Setup LSP-Zero
        lsp.preset("recommended")  -- Uses recommended configuration for LSP and autocompletion

        -- Lua language server setup
        require('lspconfig').lua_ls.setup {
            settings = {
                Lua = {
                    diagnostics = {
                        globals = { 'vim' }
                    }
                }
            }
        }

        -- Ensure LSP servers are installed
        lsp.ensure_installed({
            "pyright",        -- Python
            "lua_ls",         -- Lua
            "bashls",         -- Bash
            "clangd",         -- C
        })

        -- LSP setup (with automatic configuration)
        lsp.setup()

        -- nvim-cmp setup with additional sources
        local cmp = require("cmp")
        cmp.setup({
            sources = {
                { name = "nvim_lsp" },
                { name = "buffer" },
                { name = "path" },
                --{ name = "cmdline" }, commenting this out because it continues to auto complete random commands
            },
            mapping = {
                ["<C-Space>"] = cmp.mapping.complete(),  -- Trigger completion manually
                ["<C-n>"] = cmp.mapping.select_next_item(), -- Move to next item
                ["<C-p>"] = cmp.mapping.select_prev_item(), -- Move to previous item
                ["<CR>"] = cmp.mapping.confirm({ select = true }), -- Confirm selection
            },
        })

         -- Filetype-specific configuration for C (optional, restrict sources)
        cmp.setup.filetype("c", {
            sources = {
                { name = "nvim_lsp" },
                { name = "buffer" },
                { name = "path" },

            },
        })

        -- LSP key mappings for navigation and actions
        local function buf_set_keymap(mode, lhs, rhs, opts)
            opts = opts or { noremap = true, silent = true }
            vim.api.nvim_buf_set_keymap(0, mode, lhs, rhs, opts)
        end

        -- Code completion using nvim-cmp (no need for manual `<C-Space>` mapping here)
        -- LSP navigation
        vim.keymap.set("n", "gd", "<cmd>lua vim.lsp.buf.definition()<CR>", { noremap = true, silent = true })
        vim.keymap.set("n", "gD", "<cmd>lua vim.lsp.buf.declaration()<CR>", { noremap = true, silent = true })
        vim.keymap.set("n", "gt", "<cmd>lua vim.lsp.buf.type_definition()<CR>", { noremap = true, silent = true })
        vim.keymap.set("n", "gr", "<cmd>lua vim.lsp.buf.references()<CR>", { noremap = true, silent = true })
        vim.keymap.set("n", "K", "<cmd>lua vim.lsp.buf.hover()<CR>", { noremap = true, silent = true })

        -- LSP actions
        vim.keymap.set("n", "<leader>rn", "<cmd>lua vim.lsp.buf.rename()<CR>", { noremap = true, silent = true })
        vim.keymap.set("n", "<leader>ca", "<cmd>lua vim.lsp.buf.code_action()<CR>", { noremap = true, silent = true })
        vim.keymap.set("n", "<leader>f", "<cmd>lua vim.lsp.buf.formatting()<CR>", { noremap = true, silent = true })
        vim.keymap.set("n", "<leader>e", "<cmd>lua vim.diagnostic.open_float()<CR>", { noremap = true, silent = true })
        vim.keymap.set("n", "[d", "<cmd>lua vim.diagnostic.goto_prev()<CR>", { noremap = true, silent = true })
        vim.keymap.set("n", "]d", "<cmd>lua vim.diagnostic.goto_next()<CR>", { noremap = true, silent = true })

        -- Signature help (completion help)
        vim.keymap.set("i", "<C-k>", "<cmd>lua vim.lsp.buf.signature_help()<CR>", { noremap = true, silent = true })

        -- Refactor code... in python atleast.... but i think everything will be effected.
        vim.keymap.set("n", "<leader>rn", vim.lsp.buf.rename, { desc = "Rename symbol" })

    end,
}

