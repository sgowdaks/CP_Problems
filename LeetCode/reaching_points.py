class Solution:
    def reachingPoints(self, sx: int, sy: int, tx: int, ty: int) -> bool:
        #math way
        while tx >= sx and ty >= sy:
            if sx == tx and ty == sy:
                return True
            
            if ty > tx:
                ty = ty % tx
            else:
                tx = tx % ty
        
            if sx == tx:
                if (ty - sy) % tx == 0:
                    return True
                else:
                    return False
            
            if sy == ty:
                if (tx - sx) % ty == 0:
                    return True
                else:
                    return False
        
        return False
                
        
        
        #recursive way
#         def recurse(sx, sy, tx, ty):
#             # print(sx, sy, tx, ty)
#             if sx == tx and sy == ty:
#                 return True
#             elif sx > tx or sy > ty:
#                 return False
            
#             one = recurse(sx+sy, sy, tx, ty) 
#             if one:
#                 return True
#             two = recurse(sx, sy+sx, tx, ty)
#             if two:
#                 return True
#             return False
        
#         return recurse(sx, sy, tx, ty)
                
        
