/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let dct = {}
    for (let i = 0; i < nums.length; i++){
        if (dct[nums[i]] != undefined){
            return [dct[nums[i]], i]
        } else {
            dct[target - nums[i]] = i
        }
    }
    
};