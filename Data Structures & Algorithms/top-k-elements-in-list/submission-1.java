class Solution {
    public int[] topKFrequent(int[] nums, int k) {

        // create a hashmap where the key is the number from nums and the value is how many times it appears in nums
        HashMap<Integer, Integer> HashMap  = new HashMap<Integer, Integer>();

        // go through each number in nums
        for(int i = 0; i < nums.length; i++){
            // check if current number is a key in the hashmap
            if(HashMap.containsKey(nums[i])){
                // update value at the existing key by 1
                HashMap.put(nums[i], HashMap.get(nums[i]) + 1);
            } else {
                // write a new key with value nums[i] and give it 1 appearance
                HashMap.put(nums[i], 1);
            }
        }

        // create new arr to return
        List<Integer> output = new ArrayList<>();

        // do this k times
        for(int i = 0; i < k; i++){
            // get the max value in hashmap
            int maxVal = Collections.max(HashMap.values());
            // find the key with that value
            int maxKey = Collections.max(HashMap.entrySet(), Map.Entry.comparingByValue()).getKey();
            // push key into output list
            output.add(maxKey);
            // remove key from hashmap
            HashMap.remove(maxKey);
        }

        return output.stream().mapToInt(Integer::intValue).toArray();
    }
}