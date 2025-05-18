#!/usr/bin/env luajit

-- Enable JIT compilation
jit.on()

local function process_args()
    if #arg == 0 then
        print("Usage: " .. arg[0] .. " [name]")
        print("If no name is provided, it will use 'World'")
        return "World"
    end
    return arg[1]
end

local function main()
    local name = process_args()
    print("Hello, " .. name .. "!")
    print("Running as compiled binary with LuaJIT!")
    print("JIT Status: " .. (jit.status() and "Enabled" or "Disabled"))
    print("Current time: " .. os.date())
    
    -- Demonstrate some Lua features with JIT optimization
    local numbers = {1, 2, 3, 4, 5}
    print("\nNumbers array:")
    for _, num in ipairs(numbers) do
        print(num)
    end
end

main() 