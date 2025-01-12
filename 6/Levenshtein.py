#6. **Skriv en algoritm för att beräkna Levenshtein-avståndet mellan två strängar.**

def levenshtein_distance(str1: str, str2: str) -> int:
    """
    Calculate the Levenshtein distance between two strings.
    
    Args:
        str1: First string
        str2: Second string
        
    Returns:
        The minimum number of single-character edits needed to transform str1 into str2
    """
    # Create a matrix of size (m+1)x(n+1) where m and n are lengths of str1 and str2
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize first row and column
    for i in range(m + 1):
        dp[i][0] = i  # Cost of deleting characters from str1
    for j in range(n + 1):
        dp[0][j] = j  # Cost of inserting characters from str2
        
    # Fill the rest of the matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]  # No operation needed
            else:
                dp[i][j] = min(
                    dp[i-1][j] + 1,    # Deletion
                    dp[i][j-1] + 1,    # Insertion
                    dp[i-1][j-1] + 1   # Substitution
                )
    
    return dp[m][n]

# Example usage
if __name__ == "__main__":
    str1 = "kitten"
    str2 = "sitting"
    distance = levenshtein_distance(str1, str2)
    print(f"Levenshtein distance between '{str1}' and '{str2}': {distance}")
