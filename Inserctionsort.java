public class Inserctionsort{
    //O(n^2) 
    //prendiamo il (k+1)esimo elementonell'arrat e lo inseriamo nella sua posizione corretta rispetto ai primi k elementi già ordinati
    public static void main(String[] args) {
        int[] nums= {7,2,4,5,3,1};
        print(nums);
        for(int k=0;k<6;k++){
            int p=nums[k];           
            for(int j=5;j>k;j--){
                if(nums[j]<p){
                    p=nums[j];
                    nums[j]= nums[k];
                    nums[k]=p;
                    

                }
            }

            
            
            print(nums);

        }
    }


public static void print(int[] array){
    String s="";
    for(int el:array){
        s+=el+" ";
    }
    System.out.println(s);
}}