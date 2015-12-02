public class Solution {
   //接口Comparable 用于进行Arrays.sort排序
   	static class Pair implements Comparable<Pair>{
        int value,index;
        public Pair(int v,int id){
            value=v;
            index=id;
        }
        @Override
      //compareTo 配合接口使用
        public int compareTo(Pair b) {
            return this.value - b.value;
        }
        
    }
    public int[] twoSum(int[] nums, int target) {
        int[] res=new int[2];
        Pair[] pairs=new Pair[nums.length];
        for(int i=0;i<nums.length;i++)
        {
            pairs[i]=new Pair(nums[i],i+1);
        }
        Arrays.sort(pairs);
        
        int left=0,right=nums.length-1,sum=0;
        while(left<right)
        {
            sum=pairs[left].value+pairs[right].value;
            if(sum==target)
            {
                res[0]=pairs[left].index;
                res[1]=pairs[right].index;
                if(res[0]>res[1])
                {
                    int k;
					//必须比较，因为有可能是负数
                     k=res[1];
                    res[1]=res[0];
                    res[0]=k;
                }
                break;
            }
            else if(sum>target)
               right--;
            else
               left++;
        }
        return res;
    }
}
