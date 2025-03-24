# image[sr][sc]
# image[1][1]

# image[0][1]
# image[2][1]
# and
# image[1][0]
# image[1][2]

# change the color of the sr and sc if it matches
# call recursive(iamge) - which will mutate the image
# return image

class Solution:
    def floodFillChad(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        orig = image[sr][sc]

        if orig == color:
            return image

        def fill(r, c):
            if (r < 0 or r >= len(image)) or (c < 0 or c >= len(image[0])):
                return

            if image[r][c] != orig:
                return
            
            image[r][c] = color

            fill(r - 1, c)
            fill(r + 1, c)
            fill(r, c - 1)
            fill(r, c + 1)
        
        fill(sr, sc)
        return image
    