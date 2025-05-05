BLEU measures the precision of n-grams in a candidate translation compared to a reference translation. The precision is calculated as the number of n-grams in the candidate translation that are also present in the reference translation, divided by the total number of n-grams in the candidate translation. The formula for BLEU is:
bleu = BP * exp(∑(p_n) / N)

1. Count n-grams in the candidate translation.
For each n from 1 up to N, extract all n-grams in the candidate.
2. Count all n-grams in the reference translation.
Extract all n-grams in the reference.
3. Clip counts 
For each distinct n-gram in the candidate let: 
- count_c = min(count_in_candidate, max(count_in_reference))
This prevents the candidate from getting credit for n-grams that are over-represented in the reference.

Questions: 
- What n-grams are considering in the candidate translation when counting?
- Why do we count all the n-grams in the reference translation?
- Why n-grams in the candidate translation are clipped?
- What does clipping do?
- Explain the formula for BLEU.
- What does count_c represent?
- How do we compute the precision p_n?
- Explain the correctness of the formula p_n = count_c / count_t.

