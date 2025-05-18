#!/usr/bin/env lua

-- A simple standalone Lua application
local function main()
    print("Hello from standalone Lua!")
    print("Current time: " .. os.date())
    
    -- Demonstrate some Lua features
    local numbers = {1, 2, 3, 4, 5}
    print("\nNumbers array:")
    for _, num in ipairs(numbers) do
        print(num)
    end
end

main() 