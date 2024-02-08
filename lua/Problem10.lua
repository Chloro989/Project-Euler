local max_number= 2*1000000
local prime_numbers = {}
local sqrt = math.sqrt

function table.contains(table, element)
    for _, value in pairs(table) do
        if value == element then
            return true
        end
    end
    return false
end

local function isPrime(N)
    for i=2,sqrt(N) do 
        if N%i == 0 then
            return false
        end           
    end
    return true
end

local function PrimeNumbersUnder(N)
    for j=2,max_number do
        if isPrime(j) == true then
            table.insert(prime_numbers, j)
        end 
    end
end

local function sumPrimes(prime_numbers)
    local sums = 0
    for _, prime in ipairs(prime_numbers) do
        sums = sums + prime
    end
    return sums
end

PrimeNumbersUnder(max_number)
print(sumPrimes(prime_numbers))