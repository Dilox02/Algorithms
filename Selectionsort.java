public class Selectionsort{
    //O(n^2)
    //scegliamo il minimo degli (n-k)elementi non ancora ordinati e lo assegniamo alla posizione (k+1)
    public static void main(String[] args) {

    int[] nums= {7,2,4,5,3,1};
    print(nums);
    for(int i=0;i<6;i++){
        int m=i;
        for(int j=m+1;j<6;j++){
            if(nums[j]<nums[m]){
                int var=nums[m];
                nums[m]=nums[j];
                nums[j]=var;
                continue;
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