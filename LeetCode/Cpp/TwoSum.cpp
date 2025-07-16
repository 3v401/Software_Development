#include <iostream>
#include <vector>
#include <unordered_map>

// Same logic as in Python solution

std::vector<int> TwoSum(const std::vector<int>& nums, int target){
    std::unordered_map<int, int> hash;
    
    for (int i=0; i<nums.size(); ++i){
        int complement = target - nums[i];

        if (hash.count(complement)){            // If complement in dictionary hash
            return {nums[i], complement};
        }
        hash[nums[i]]=i;                        // Store {value: index}
    }
    return {};
}

int main() {
    std::vector<int> nums ={2, 7, 11, 15};
    int target = 9;
    std::vector<int> result = TwoSum(nums, target);
    std::cout << result[0] << ", " << result[1] << std::endl;
    return 0;
}