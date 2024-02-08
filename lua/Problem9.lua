local list = {}

for a = 1, 999 do
    for b = a + 1, 999 do
        local c = 1000 - a - b
        if c > b then  
            if a^2 + b^2 == c^2 then
                table.insert(list, a * b * c)
                print(a,b,c)
                break
            end
        else
            break
        end
    end
end

for i = 1, #list do
    print(list[i])
end