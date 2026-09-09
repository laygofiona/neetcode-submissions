class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        // to be an anagram, the string must have the same character length and must have the same characters
        
        // use a hashmap where the key is the sorted string and the value is a list of anagrams of that string
        HashMap<String,List<String>> HashMap = new HashMap<>();

        // go through each string in strs
        for(String s: strs){
            // convert the current string to a character array so we can sort it
            char[] my_chars = new char[s.length()];
            my_chars = s.toCharArray();
            Arrays.sort(my_chars);
            // then convert it back to a string
            String new_str = Arrays.toString(my_chars);

            // check if hashmap contains the sorted new_str
            // if it doesn't then we want to add it to the hashmap where the key is the new_str and the value is s
            // else, it contains the new_str as a key
            // so we just add s as a value to the existing key
            if(!HashMap.containsKey(new_str)){
                // create a new list
                List<String> new_list = new ArrayList<>();
                new_list.add(s);
                HashMap.put(new_str, new_list);
            } else {
                List<String> old_list = HashMap.get(new_str);
                old_list.add(s);
            }

        }

        // return a list with the hashmap values
        return new ArrayList<>(HashMap.values());
       
    }
}