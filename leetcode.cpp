#include <unordered_map>
#include <vector>

using namespace std; // NOLINT

struct _1 {
    vector<int> twoSum(vector<int> &nums, int target) {
        unordered_map<int, int> seen;
        for (int i = 0; i < nums.size(); ++i) {
            if (seen.count(target - nums[i]))
                return {seen[target - nums[i]], i};
            seen[nums[i]] = i;
        }
        return {};
    }
};

int main() {}
