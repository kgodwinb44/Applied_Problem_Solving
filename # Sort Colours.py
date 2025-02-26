# Sort Colours

class Solution():
    def sortColors(self, nums):
        
        # Index
        # Red = 0
        # White = 1
        # Blue = 2

        # Create pointer variables, white current, red start, blue end
        white = 0
        red = 0
        blue = len(nums) -1

        # While white is less than blue
        while white <= blue + 1:
            print(nums)
            print(white)
            print(red)
            print(blue)
            # Current number = 0? if yes, move white pointer next and place red at start
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                red += 1
                white +=1
            # Current number = 1? if yes, move white pointer next
            elif nums[white] == 1:
                white +=1
            # Current number = 2? if yes, placed at end of list, check new pointer value
            else:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -=1

sol = Solution()
numbers = [2,0,1]
sol.sortColors(numbers)



        
            
            
            
        
            
            
            
            