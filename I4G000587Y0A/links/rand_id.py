from uuid import uuid4

def generate_random_id() -> str:
    """
    Function that generates a random 8 character string. 
    Useful for creating random Ids for URLs and objects.
    """
    # generating id
    id = str(uuid4())
    
    # first 8 characters of id 
    id = id[:8]
    
    return id