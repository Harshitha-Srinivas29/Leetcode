class Data{
    String val;
    int timestamp;

    Data(String val, int timestamp){
        this.val = val;
        this.timestamp = timestamp;
    }
}
class TimeMap {
    HashMap<String, List<Data>> map;
    public TimeMap() {
        map = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        if(!map.containsKey(key)) 
            map.put(key, new ArrayList<Data>());
        map.get(key).add(new Data(value, timestamp));
    }
    
    public String get(String key, int timestamp) {
        if(!map.containsKey(key)) return "";
        List<Data> data = map.get(key);
        return findClosest(data, timestamp);
    }

    public String findClosest(List<Data> data, int timestamp){
        int left = 0, right = data.size() - 1;
        String res = "";
        
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (data.get(mid).timestamp <= timestamp) {
                res = data.get(mid).val;
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return res;
    }

}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */