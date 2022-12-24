def histogram(nums):    
     for x in nums:
        output=""
        times=x
        while times>0:
            output=output+"*"
            times=times-1
        print(output)

histogram([1,2,3])