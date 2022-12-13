from __future__ import division
from fractions import Fraction
from hashlib import blake2b
from dnds import dnds, pnps, substitutions, dnds_codon, dnds_codon_pair, syn_sum, translate
Balanophora_plastid = "TTTTATTATATATTTTGGTATTTTAAAAATAAAAAATATACATTAAAAAATAAAAATCTATTTCAAATTAAATGGTAAAAATTTATTATATATAATTATTATATAATTAAAAAAATAATTTAATATCAAAATTATAAATACTTTTAGTATAGTATAAAATAATAAAAAGGAGGTTAATAATTTAAAAAATAAAAATGTTAATAATTTATAATTATTTATATAAACAACAAAAAATATATTTTATTGGAATTTTTTTTGGTTTACAATATGGATTTTTTAATATTATTTATAATTTTTTATTTTTAAAAAAATTTAATAATAATATTATTAGTTATAAAAATAAAAAAAATAATATATTTTTATTTAATATTATTAATATATGTTTATATTATTTTTTTTATTTTTATATTTTAATAAATTTAAAATATTTAAAATATTTTCATTTATTAAATATATTAATTATTCCTTATATATTAATATTATTATTTAATAATAATATTAATATATTTTTTTTTATACAAATTTTAAAATTATTAAAATTTTTTATTATTCCTATTTTTATATTTAATAAATTAATATATATATATATATATAATAAATATGTTAATTTATTTAGTATTATTTTTGGTTATTTTTTTAGTTATTTATTAATATTTTTATTTAATAAATTAATAAATATTAATAAATTAATAAATATTAATAAATTAATAAATATTAATAAATTAATAAATATTAATAAATTAATAAATATTAATAAATTAATAAATATTAATAAATTAATAAATATTAATAAATTAATAAATATTAATAAATTAATAAATATTAATAAATTAATAAATATTAATAAATTAATAAATATTAATAAATTAATAAATATTTTATTATTTATTATATATATATATATTTTTGGAAAAATATCTATACCTATATTTATAAATAATACAAATTTATTTTATTATAATAATAAATATTATAATTATAATATTTATAATATTAATAATTATTTTATTGAATTTTTTTTTATTAATATTAAAAAATATAATCAATTTATAAAATATTTTAAGAATAATAATTTTGAAAGTAGTATTATTTTTGAAACATCACAATATTTTTTTAATTTTAATAAAAAAAAAAAAATTATAAATTTTTTTTTTTCATTTCCTTCAAGTTTATATATTTTTTATAATTTATTAAATAAAAAATATTATATAAAAAAAAAAAAAAATTATTTTAATTTTTTTAAACTAAAATTAAAATTAAATATATATATGAATATTTATATAAAAAAAAATTATTTTAATTTATATAAAAAAAAATTTTATAATAAAAAAAATTTTTTATATATAAAAAATTTATATGATCCATTATTAAATAAATTTTATAGAAAAATAATAAATATAAATAAAAAATATTATATAAAAAATAAATATAATAATAAATTAATAAAAAATATAAATAAAAATAATATATATATAAAAAATATATATATATATGAAATATTAAAAAAATTTTCAAAATATTCATATAAATTAATAAATGAATTAGAACAACAAGAAAATGAAGAAAATTTATTAGTAGATGATTATGATATTCGTTCAAGAAAATATAAAGATATTTTAATTTTTTAGTTTTTTAATAAATTAAAATATTATAATAATTTATTAAATATTAATGAATTATATTTAATAAATTATTTTAATCAATCAGATTTTGATCATGATATAATAAAAGGTTATATACGTACTTATAGACGTAAAATTTTAATATTTAATAAATTTCAATTAAAAACATATTCAAATATATTTTTTTATAAATTTAAAAAAATATATTATAAAATAAATAATAATAATATTATAAAATTAGATTTTTAGAATTCAATTATTTTAACTAATATAATAAAAAGTTTAGTATTAATAATTCAATCAATTTTTAGAAAATATATAAAAATACCTTTTATAATAATTATAAAAAATATATTTTTATTTATTATTAAAATTTTTTATAAAAAAAAATCTACTGAATAGTTTAATGATTTTTTAAAGTAGAAAAAAGAAACACATATTTTATGTACTTTTAAAAAAATTCCTTTATTAAATTTAAATAATAATTATAAATATAAAGAATTTTCAAAAAATTATATTATTTATATTATGGAAGGTATAAAAATTAAAATATTATATCCTTATATTTATAATAAAAATAATAATAATAATTATTTTTTTTTAAAAATTTTTGGTATAAAAAAATCAAAATTTATTTTTAAATATTTTAAAAAAAATTTATATATTAGTATTTTTAAAAATAATTATATATTAATATATATTTATATTTTAAAATATTTAAAAATAAATTTATTATTATTTTTATTAAAAATAATAAATATAAAAAATAATAATAATATAAATAATATTATAATAATAAATTTATTTTTAAATATTTTAAAATATAAAAAAAATAAAAAAAAATATTTTAATAAATTAAAAAATAAGAAATATTTATATTTTAATAAATTTAAATATAAAAAAAATAAAAAAAAATATTTTAATAAATTAAAAAATAAGAAATATTTATATTTTAATAAATTAATAAATTTTAATATTTATCAATTAAAATATAATAATAATTATAATATAAAAATAATAAATAATATTAAAATTTATAATAATTATAATATTAATTTATTTTATTATTTTTTTTTATCATATATAAAAAAAAATGAAATAAATTTAGAAATTTTATTAAAATATAAAAAAAATAATTTTTCTATATTTTTTAAAAAAAGTATTTTATTAATTGATTCTATTTGTATATTTAATAATAATTTTAATAAAAATTTTTATTATAATATAATTTTTAAAAATTATATTATAATAAAAAATAGTAATATTTTTTATTTTTATTTTAAATTACCTGAAAATATTTTTTTTTTAAAAAAAATAA"
Cuscuta_reflexa = "CGGGAATTGAACCCGCGCATAGTGGATTCACAATCCACCGCCTTAATCCACTTGGCTACATCCGCCCCAGACTATGCTACGAATTTCAAATTAAAAAGGAGCAATATGGTTATTGCTCCTTTATTTTCAATTTATTTTGAAAAACTCCTATACACTAACACCGAATTCTTATCCATTTGTAGCTGGAGCTTCAATAGCAGCTAGGTCTAGAGGGAAGTTGTGAGCATTACGTTCATGCATAACTTCCATACCAAGATTAGCACGATTAATGATATCAGCCCAAGTATTAATTACCCGGCCTTGGCTATCAACTACGGATTGGTTGAAATTGAAACCGTTTAGGTTAAAGGCCATAGTGCTGATACCTAAAGCAGTGAACCAGATACCTACTACAGGCCAAGCAGCTAAGAAGAAGTGTAACGAACGAGAGTTGTTGAAACTAGCATATTGGAAAATCAATCGGCCAAAATAACCATGAGCGGCTACGATATTGTAAGTTTCTTCCTCTTGACCGAATCTGTAACCTTCGTTAGCAGATTCATTTTCTGTGGTTTCCCTGATCAAACTGGAAGTTACCAAGGAACCATGCATAGCACTGAATAGGGAACCACCGAATACACCAGCTACGCCTAACATATGAAATGGGTGCATAAGAATGTTGTGCTCGGCCTGGAATACAATCATGAAATTGAAAGTACCAGAGATTCCTAGAGGCATACCATCAGAAAAACTTCCCTGACCAATTGGATAGATCAAGAAAACTGCGGTAGCAGCTGCAACAGGAGCTGAGTACGCAACAGCAATCCAAGGGCGCATACCCAAACGGAAACTCAGTTCCCACTCACGACCCATGTAACAAGCTACACCAAGTAAAAAGTGTAGAACAATTAGTTCATAAGGACCACCGTTGTATAACCATTCATCAACAGACGCCGCTTCCCATATTGGGTAAAAGTGTAAACCTATAGCTGCAGAAGTCGGAATAATGGCACCCGAAACAATATTGTTTCCGTAAAGCAGAGATCCAGAAACAGGTTCCCGAATACCATCTATATCTACTGGAGGAGCAGCAATGAAGGCAATAATAAATACAGAAGTTGCGGTCAATAAAGTAGGGATCATCAAAACGCCAAACCATCCAATGTAAAGACGGTTTTCAGTACTGGTTATCCAGTTACAGAAACGACCCCATAGGCTTTCGCTTTCGCGTCTCTCTAAAATTGCAGTCATGGTAAATTCTTGGTTTATTTAATCATCAAGGACTCCCAAGCACACAAATTTTCTAAAAAAAAAAGTAAAACATGCAAGGCTTGTTATTCAACAGTATAACATGACTTAGATGCTCGTGTCAACGTCAACCAATAAACCAAAATCTATCTCTTCCAATCTTTTGGAACCCAATTGAAAGTAAGTGGATTAAAAAAAAAATTTATATTGCTTTAGTTTTTCATTGCACACGGCTTTAGCCTCGGGTAAATTTTCATTTATCATTTTGAATCAAGATTTCAGATTATAGTGGAAAAAGACAACCTTAAGAATTTATTCAAAATTTGATTTTAAGAATATTGAAGATTGAAGACTGAATCATTAAAAATTGGCCTGCTCATTGATATAAACTATATCAAAATACCAAATCCGCCCTTTCGACACTCCTCGCAAATTCAACGAAGCGTTTGGGAAAGTTAAAAAAATAATTTGCTCTTCCGACGTAAAGAATTCTTCCAATAATTTTAGGCCCAAGCTTTGTAAAAAACCGCGTAGAGTACTTTTGTGTTTACGAGCTAGAGTTCGAGCACAAGAAAGTCGAAGTATATACTTTATTTGATACAAACTCCTTTTCTTGGAAGATCCACTATAATAATGAAAAATATTTCTGCATATACGCCCAAATCGTTCAATAATATCAGAATCTGAAAAATCGGCCCAAACAGGTTTACTAATGGGATTTCCTAGTAGATTACAAAATTTAGCTTTAGCTAAGGATCCTATAATAGGAATAATTGGAACAAAAGTCTCGAATATCTTCATATCATTATTTATTAAAAACAAATTTTCTAGCATTTTGCTCCGTACCATTGAGGGGATTTGTGCAATACTTGAAATATAGTCCATAAGATAAAAGGGGTGGCTGTCTATTTGACTTATATTTATTCTTTCGGTATGGAACCACAGATAAAAATAACATTGCCAAAAATTGACAATATAATATTTCCATTTAGGCATCAAAAGAAGCCCCCCGTTGGATGCCAGAATTGATTTTCCGCGATACCGAGCATAATGCATTGAAGGGTCCGTATCCTTGAACAAACGTAGGTTTGCTTGCGAATCCTGAGCAAAAAGTTCTGCAAAGCATTCTATTTTTCCATAGAAAATATTTCGTTCAAAAAGGGTTACAAAACTCATTGATCCTAAATGAAGAGATTGGTTACGGAGAACTAAAAAAATGGATTCGTATTCACATATATAAGAGTTATACAATAAGAAGAGAAATCGTTCATTTCTTTTTGACTTATTTGTAGTAATTAAACTTTTCACACTACAAAACTCGTGTAGAAAGAATCGTAATAAATGTAAAGAAGAAGCGTCTTGTACCCAATATCTAATTTTTTGAACCAATATTTCCGGATGAGGGGGGTTGGGTATTAGTAGATCTAATACATATTTTAAATGTGATAAATTATCCTCGAAAAAAGTAAATATTGAATGAATTGATCGTAAATTCTGAGATTTTAATATTTTTTTTCGCTCTGATATGAATTTGAAAAAAAACGGAATTTCAAAAAGAAAAGAAAACCCCGATGATAGCAGTTTATAATAAAAACTCTTGAGGAGCCCATAAATTGTCCTTTTGTTAGAATAATTAGAATAATAAGTAGTCAAATGTATCTGTTTATACATTCGATTAATTAAGCGTTTCACAATTTGAAAACGAAATTTTTT"
Viscum_coloratum = "ATTTTATTTTTGCTCCTTTACTTTCAATAACAATAATTAAATCAATAATGAAATGAAATAAAAAGTCTATAATACAAACGATGTATTATCCATTTGTGGATGAAATTTCAACAGCAGCTAAGTCTAGAGGAAAGTTATGAGCATTACGTTCATGCATAACTTCCATACCTAGGTTAGCACGGTTAATAATATCCGCCCAGGTATTAATTACACGACCTTTACTATCAATCACAGATTGGTTGAAATTAAAACCATTTAAGTTAAAAGCCATGGTACTAATACCTAAAGCAGTGAACCATATACATACAACAGGCCAAGCAGCAAGAAAGAAATGTAAGGAACGAGAATTGTTAAAACTAGCATATTGGAAGATTAATCGGCCAAAATAACCATGAGCGGCTACGATATTATAAGTTTCTTCCTCTTGACCGAATCTGTAACCTGCATTGGCAGATTCATTTTCTGTAGTTTCCCTGATCAAACTAGAGGTTACCAAAGAACCATGCATAGCACTGAAAAGAGAACCGCCGAAAACACCAGCAACACCTAACATATGAAAAGGGTGCATAAGGATGTTGTGCTCAGCCTGAAATACTATCATGAAGTTGAAAGTACCAGAGATGCCTAAAGGCATACCATCAGAAAAACTTCCTTGACCAATTGGATAGATCAAAAAAACGGCAGTAGCAGCTGCTACTGGAGCTGAATATGCAACAGCAATCCAAGGACGCATGCCTAGACGGAAGCTAAGTTCCCACTCACGACCCATGTAAAAAGATACACCAAGTAAGAAGTGTAGAACAATTAACTCATAAGGACCACCATTGTATAACCATTCATCGACGGATGCTGCTTCCCATATCGGATAAAAATGCAAACCAATAGCTGCAGAAGTAGGAATAATGGCACCAGAAATAATATTGTTTCCATAAAGTAGAGATCCAGAAACTGGTTCACGAATACCATCAATATCAACTGAAGGAGCAGCAATGAAGGCAATTATAAATACAGAAGTTGCGGTTAATAGGGTAGGGATCATCAAAACACCAAACCATCCAATGTAAAGGCGGTTTTCAGTGCTGGTTATCCAGTTACAGAAGCGACCCCACAGGCTTTCGCTTTCACGTCTCTCTAAAATTGCAGTCATGGTCAATTTTTGTTTGATTTATCATCAGGGACTCCCAAGCACACGAATGAAAGGATATAAAATAAAAAATTCCATTCGTGTGCTTGTTATGAAACAGTATAACATAACCGATATTGCCATGTCAACCAAATAAGGCTTGTGAATAATAAGTTACAAAAACGAATTCAATAAAAAAGATCATAATGGGTTGCCCGGGACTCGAACCCGGAACGAGTCGGATGGAGTAGAATTTCTTTATAAAACTATTTTAAAAAGGAAATAAAATTTTAAAATATAAATGAAAAAAAATCTATCCCTAAACCGCGCTTGCTTATTTCATTGCACACGGCTTTCCCTATGTATATAGTTTGTCCTCCTGTCCTTCTGGAAGAACTCTAATCTAATAAAGTAAATGAGTTGATTCACTCTTCTTAGTCTTCTGCGTGAACTGTTCATACCACATTAAAAAATGAACGGAATTTTATTATCCCCTTTTGATTGATTTATAGGTACTTTTCAGATACATGATTTGAGAATCAATCAGTGGATGAATAATAAATCAGATCCTTAATACAAATAATATCCAAATACCAAATACGTCCTCTATATGAAAACCTTCGAGAAGTATAATATTTTGAAATAATAAAGGAAAGAACATCCTCCGTAGTAAAAAAATCTTGCAAGAATACCAAACCAAATATTTTCTTCAAAAAAGAACGTACAGTCAATTTGTGTTTACGAGCAATAGTTCTAACACAAGAAAGTTGAAGAATATACTTTATTTTAAAAATACTATTTTTTTTTGAGGATCCGCTGTGATAATGAGAAATATTTCTTTGGATACACCAAAATAGGTAAAAAATCTCCGAATCCGCTAAATCCAACCATACCGACTTACTTATGGGATGCCCTAAGACATTACAAAATTTTTCTTTAGCCAATGATCCCATCAGAGAGAGAATAGGAACTGTGGTATAAAACTTATTTTTTATAACATTATCAATGATATATGAATCTTCAAGCATTTGACTCCGTACCACTGAAGGATTTAGTCGCACACTTGAAAGATAGCCTAAAAAGTGAACTGAAGTTTTCGATATATTTCTATGGAACATTGGTTGAGACCACACATAAAAACGATCTTTCCAGAAATTAGCAAGGTAATATTTCCATTTTTTCATCAGAATAGGATTTCCTTTTGAAGCCAGAATGTATTTTCCTTTATATCTAACATAATACATGAAAGGATCCTTTAAAAACCGTAGAATGTTATTAAATTCTGAAGTAACGGCAGCATGTTCTATTTTTCCATAGAAATATATTCTCTCAAGAAGGATTCTAAAAAGTGTTGATCGTAAATGGAAAGATCGGTTACGGAGAAAAACAAAAATCGATTCGTATTCACAGATATGAGAATTATATAAGAACAAGAGCAATTTTTGATTCTTTTTTGAAAGGATTGAAATAAATTTCTTTTTTGAAAAAATAAAACGATTCAAATTCAAAATTTCATAGCAAAAGAATAATCGTAAAAAATGCAAAGAATAAGCATCTTTGACCCAGTAACGAATAATTTGAACCAATATTTCCAGATGGATAGGATAAGGTATTAGTATATTTGACACACCATTTAAATGGTATAAATTGTCCTCTAAAAAAGTAAATATTGAATGAATGGATCTTACATTTTTAGATTCTTCTATTTTTTGATTAGCTTCTTTTCTAGAAGCTAAGAAGCATAAGGTAAATGGAATTTCCAAAATGACTGAAAATACCTCTTCCAGTATAATTTGAAAAAAAAAAAATTTTTATGT"
Cassytha_filiformis = "GGGCGAACGACGGGAATTGAACCCGCGCATGGTGGATTCACAATCCACTGCCTTGAGCCACTTGGCTACATCCGCCCCTCCTTTCTCTCAAAAATGGTATATAAAATGCCAATCAATCCCTTTACTTAAAAAAAAGGGTTTTGAATAACATAGTATACAAACGCTTTATTAGATTGAATAAAAGAAATGAAAATGAAAAATTCTGATGTGAATAAAACACTAATGAATCAAACGTATCAATACCAAACTTCTTGATAGAAGTTTGGTATTGACTATTCAATGTATCATATACACTAAAACCGAAGTATTATCCATTTGTGGATGGAACTTCGACAGAAGCTAGGTCTAGAGGGAAGTTGTGAGCATTACGTTCATGCATAACTTCCATACCAAGATTAGCACGATTGATGATATCAGCCCAAGTATTAATAACACGACCTTGACTGTCAACTACAGATTGGTTGAAATTGAAACCATTTAGGTTGAAAGCCATGGTGCTGATACCTAAAGCAGTAAACCAGATACCTACTACAGGCCAAGCAGCTAGGAAGAAGTGTAAGGAACGAGAATTATTGAAACTAGCATATTGGAAGATCAATCGGCCAAAATAACCATGAGCAGCTACGATATTGTAAGTTTCTTCCTCTTGACCAAATCTGTAACCTTCATTAGCAGATTCATTTTCAGTGGTTTCCCTGATCAAACTGGAGGTTACCAAAGAACCATGCATAGCACTGAATAGGGAGCCGCCGAATACACCAGCTACGCCTAACATGTGAAATGGATGCATAAGGATATTGTGTTCCGCCTGGAATACAATCATGAAGTTGAAAGTACCAGATATCCCTAGAGGCATACCATCAGAAAAACTTCCTTGTCCAATAGGGTAGATCAAGAAAACAGCAGTAGCTGCTGCAACAGGAGCTGAATATGCAACAGCAATCCAAGGACGCATACCCAGACGGAAACTAAGTTCCCATTCACGACCCATGTAACATGCTACACCAAGTAAGAAGTGTAGAACAATTAGCTCATAAGGACCACCATTGTATAACCATTCATCAACGGATGCTGCTTCCCATATCGGGTAAAAATGCAAACCGATAGCTGCAGAAGTAGGAATAATGGCACCGGATATAATATTGTTTCCATAAAGTAGAGACCCAGAAACGGGTTCACGAATACCATCAATATCCACAGGAGGAGCAGCAATGAAGGCAATAATAAATACAGAAGTTGCGGTCAATAAGGTAGGAATCATCAAAACACCGAACCATCCAATATAAAGACGGTTTTCGGTGCTGGTTATCCAGTTACAGAAGCGACCCCATAGGCTTGTGCTTTCACGTCTCTCTAAAATTGCAGTCATGGTAAAATCTTGGTTTATTCAATTATCAGGGACTCCCAAGCGCGGAGATTATCTATAAATAGAAATAGACAATGGAAGGCTTGTTAGCCAACAGTATAACATGGCTTATACGTCCGTGTCAACCAATATTAGTCTGAGTAAATCCATCAGAACAATTTGTAAATTTAATGAGTTAAAAGAAAGGTGGGGATTTATGCAATAAAAAAATTGCGTATTTTGCGTATGATTGGTAATGGAATGGGTTGCCCGGGACTCGAACCCGGAACTAGTCGGATGGAGTAGATAATTTCCTTGTTACAATAGATATAAAGTAAAAAGATCCCCCCAAAAGCCGTGCTTGCATTTTTCATTGCACAGGGCTTTACCCATGTATACATTGAAAACTCCATTCCCTAGAATGGAACCGAAGAAACTTGAATACTCAGTGGATTCAACCACTACACCACTGTATGAGCATTTCAGAATTCAAATGAATGACATTTTTTTTTTCTCCCTTCCTAATTTAAGGATCCTTTTACATAGCCTCATGACCCATCATAAATTACTAGCTAGGTCATTGATACGGAGAATATCCAAATACCAAATTCGTTCTCGATGTGACCTATAAGAATTAGAAAAGGTTCTTGGAAAGATCAAAGAAAGAACTTGTTCTTCTTCCATAAAGAATTGTTCCAAAAATTCCGAACCTAATCTTTTCAAAAAAGCACGTACCGTACTTTTATGTTTACGAGACAAAGTTCTAGCACAAGAAAGTCTAAGTATATACTTTATATGATACAAACTCTGTTTTTTTGACGATCCGCTGTGATAATGCGAAAGATTTCTGCATATTCGCCCAAATCGATTGAGAATCTCAGAATCAGGCAAATCGGCCCAAAACGACTTACTAACGGGATCCCCCGATACATTACAAAATTTGGCTTTAGCCAATGATCCAATCAGAGGAATAATCGGGACTATGGTCTCGAATTTGTTAATAGCAGTATCCATTCGAAACGAATTCTCTAACATTTGACTCCTTACCACCAAAAAGTTTAGTCGTACACTTGAAAGATAGCCCAGAAAATAGAAGGTATGATTATATAATTGCTTTATATGGATCCCGCCTGGTTGAGACCACAAGTCAAAATGACATTGCCATAAGTTGACAAGGTAATATTTCCATTTCTTCATCAGAAGATGAGTCCCCTTTGAAACCAGAATGGCTTTTCCTTTATATCTGGCATAATGCATGAAGGGTTCTTTGAACAACTCTAGGATTTTCTTAAAATCATTACAAAAAACTACTACAAGATGCTCTATTTTTTCATAGAAATGGATTCGCTCAAGAAATAATCCAAAAGATGTGGATCGTAAATGAAAAGATTGTTTACGGAGAAACATAAATATGGATTCATATTCATACACATGAGAATTAGATAGAAACAAAAATAATCTTTGATTTTCTTTTAAAAAAAGGGAAATGGATTTTTTTTTAATAATGAGACTATTTGAATTCCAATACTCGTAGAGAAGAAATCGCAATAAATGCAACGAGGGAGCATCTTGTATCCAAGAGTAAAGGATTTGAA"
Orobanche_crenata = "TCGTTACGCCCTGTTATATAAATAGATAAATAACTTCAAAATAATACTCAATTATTAATCAATCCCCCAAAAGTCTATTATATTTTCAAAACCTCCTATAAACTAAGACTAAGTCTTATTGTTGGGCTTCTCTCGAAGCTAGATCTAAAAGGAAGTTATGAGCATTATGTTCATGCATAACTTCCATCCCATACTAAGGTTAGCACCGTAAGACTTGTTATTCACCAGTAATGACTTATATATTCGTGTTAACAAATCTCAATAACTATATTAATCTATTCAAGCAGATTACAAAAAAAAATACGGATAATAGAATTTATAATTTTAATATGACGGTGGGTTGCCCGGGATTTGAACCCGGAACCAATCGGATGGAGTAGATAATTTCTTTGTTATGTTAGTTAAATAAAGAAAAATCCCTCCCCAAGCTGTGCTTGCAGTTTTCACTGCACACGGCTTTCCCTATGTATACATCATTTTCCGTTCTTATAAAGAAACTTATTTAAATCAATTGAATATTCAATTGATTTAACCCTTATTACATATTACATACTATATAAACATTTCAGAATAGTATAAATCCATGAATAAATTTTATTTTCAAAATTTCATTATTTGTAATCGGCCATATCATTAATAAAAACAATATCCAAATACCAAATTCGACTTCTATATAATTCCTGTAAACTCGAAGAAGCTTTTGGGAATGTCAAAAAAAGAACGTTTTCTTTCGTCATAAAAAATTCTTCTAATAATTCCGAGTCAAATCTTTTCAAAAAAGTACGTAGAGTCCTTTTGTGTTTCCGAGCCAAAGTTTTAGCACAAGAAAGTTGAAGTATATACTTTATTCGATACAAACTTTTTTTTTTTGAAGATCCACTATGATAATGATAAAAATTTCTGCATATAGACCCAAATCGATCAATAATATTAGAATCTGATAAATTAGCCCAAACTGACTTACTAATGGGATGCCCTAATACGTTACAAAATTTCGCTTTAGCCAATGAAGCAATCAAAGGAATAATTGGAACAAAGGTATCGACTTTATTAATAGCATTATTGATTAGAAATGAATTTTCTAGAATTTTACTCCGTATCACTGAAGAGTTCATTCGCAAGCTTACAAGATAACCTAAAAATTCAAAAGACTGATTGTATAATTGGTTTATATAAATCCTTCTAGTAGAAAACCACAGAAAAAAATAACATTGCCAAAAAGTAATCAAGTAAAATTTCCATTTATTCATGAAAAAGGGCGTCCCTTTTGAAGCCAGAATGGATTTTCTTTGATACCTAATATAATGAAAACAAGGTTCCTTGAACACCCATAGGTTTACTTGAAAATCCTTAACCTTTACAAAAGCATTCACAAAATATTTTATTTTTACATAGAAATATATTCGTTCAAGAAGAACTCCAAAGGATATTGATCGTAAATGATAAGATTGGTTACGTAGAAAGACGAAAATATATTCGTATTCACATACATGAGAATTATATAAGAATAAGAATAATCTTTGATTACTTTTTGCAAAAAAATAACTGGCTTTCTTTGGAGTAATAACACTATTCCAATTTTTGTTGATAAAGAATCGTAATAAATGCAAAGAAGAGGCATCTTTTATATAATATCGAAGAGTTTGGACCAAGATTTCCGCATGGACCAAGTGGGGTATTAGTATATCTAATACTAAATTTAAATGTGAAAAACTATCCTCTAAAAATGGAAATATTGAATGAATTGATCGTAAATTCTGCGATTTTACTATCTTTTTATTTTTCTCTTCTAGACAAGATATTAATCGTAGAGAAAATGGAATTTCCACAATAAAAGAAAGCCCCTCTGATATGATTTCAGAATACCAACTTTTGGTGCGCATTAAAAATGGAGTTTGATTAGAAGCATTATAAGAAATAAAAAAATAATTCTGTTGATACATTCGAGTAATTAATCGTTTCACAATCAGTAAACTGGATTTATTGTCATAACCTAAACTTTTCGAAGAAATAAAAATAGATCTACCTAAACCACGATCATGAGCAAATGAATAAATATACTCCTGAAAAATAAGTGGATATAGGAAACGGTGTTGTTGAGATCTTTCTAGTTGTAAATATTTTTGGATTTCTTCCATTTGAAATTTAAATCAAAAGTAGAAAATTTTGTGGGTTATCAAATGATACATAGTACGATATAGTCAAAACAAGCTATTCTAGTCAGAATAGATACCTCGAGGTAAAATTATCAACAGACTCTCTACCCTCCCCTTATTCCTATTCATTTACTTTAATTCGTCTATGTTATAGGATAAACAAGATGTTTAGAAATCTTTTATTTTATAAACCTAATCGCTCTTTTGATTTAGGAAAAACTTTCTTAATCAATATACTACTTCTTTTACACACGCATTTTCATTTCATACTAGAGAATGTTAATAGTTAGGATTCATTAAAAAATATAGATCCACTCGTGGGGGAGAAGTCCTTACCGTATCAGGCACTAATCTATTTTTAACGTCTAATTAGATCGGTAAATTATTCAAATTAAGAATAGAAGCTGGTTGCTTTTTCTTTCTAATAATGAATTGAAGCCCTGAGGCCTTATCCATCTATTCATCCGACCAAACTTTATTTTGTTCCATTGCAAGAATTCAAACAAGATTTTATACCAATACTAGAGGAATCAAATATCCTCAAAACTCTCCATTGATACGACATGCTATTTTTTCCATTTATTCCCTTTTACGGATCAGTCGTGGTCTTCCAAACTAATGGTATGGACGAATTCTTCACTTCATCCAAATGTGTAAAAGATTATAGTCGCACTTAAAAGCCGAGTACTCTACCGTTGAGTTAGCAACCCGAATAAAATAGAGATTAAACAAAACTTCAAATAAAAACTAAAGGATGTATATATACAATCGATCAAAATAAATT"
Orobanche_gracilis = "ATCATCCATACATAACGAATCAGTGTGATGTGATATATATATATTCATATCATATACGTAATATCTGAACAGTAAAGTAAAAAGTAGTGGGCGAATGACGGGAATTGAACCCGCGTAATGATGAATTCACAATCCAGTGCCTTAATCCACTTGGCTACATCCGCCCCCTACTATTACTATTTTACTATTTAATTCATTTAAAAATTTAAATAAATTAAATAATAATAAATTTAAAGCAAATTACAAAAAGAAAATATGGATCATAGAATTTATAATTTCAATATGAGGGTGGGTTGCCCGGGATTCGAACCCGGAACTAGTCGGATGGAGTAGATAATTTCTTTGTTATAGTTATATTAGTTATATAAAGAAAAATCCCTCCCCAAGCCGTGCTTGCAATTTTCACTGCACACGGCTTTCCCTATGTATACATCATTTTACTTAGAAATAGACTTTATTTAAAAAGTTGAATATTCAATTGATTTAACCCTTATTACATACTATATAAAATAAACATTTCAGAATAATATAAAATCCATGAATAAATTTTATTTTAAAAATTTAATTATTATTATTTGTAATCGGACATATATCATTAATAATAAAAATATCCAAATACCAAATTCGACTTCTATATACTTCCTGTAAACTGGAAGAAATTTTTGGGAATGTCAAAAAAATAATGTTTTCTTTCGACATAAGAAATTCTTCTAATAATTTCGAGTCAAATCTTTTCAAAAAAGTACGTAGAGTACTTTTGTGTTTCCGAGCCAAAGTTTTAGCACAAGAAAGCTGAAGTATATATTTTATTCGATACAAACTTTTTTTTTTTGAAGATCCACTATGATAATGATAAAAATTTCTGCATATAGACCCAAATCGGTCAATAATATTAGAATCTGATAAATCAACCCAAACTGGCTTACTAATGGGATGTCCTAATACGTTACAAAATTTAGCTTTAGCCAATGAAGCAATTAAAGGAATAATTGGAACAAAGGTATCGACTTTATTAATAGCATTATTAATTAGAAATGAATTTTCTAGTATTTTACTCCGTATTACTGAAGAGTTTCTTCGCAAACTTAAAAGATAACCTAAAAATTCAAAAGAATAATTGGATAATTTATTTATATAAATCCTTCTTGTATAAAACCACAAAGAAAAATGCCATTGCCAAAAAGTAATCAAGTAAAATTTCCATTTATTCATGAAAAAGGGGGTCCCTTTTGAAGCCAGAATGAATTTTCTTTGATACCTAATATAATGAAAGCAAGGTTCCTTGAACACCCATAGGTTCTCTTGAAAATCCTTAACCTTTATAAAGACATTCATAAGATATTTTATTTTTCCATAGAAATATATTCGTTCAAGAAGAACTCCAAAAGATATTGATCGCAAATGATAAGATTGGTTACGTAGAAAGACGAAAATATATTCGTATTCACATACATGAGAATTATATAAGAATAAGAATAATCTTTGATTACTTTTTGCAAAAAAAGAACTGGCTTTCTTTGGAGTAATAAAACTATTCCAATTTTTGTTGATAAAGAATCGTAATAAATGCAAAGAAGAAGCATCTTTTATCCAATATCGAAGAGTTTGGACCAAGATTTCCGCATGGACCAAGTGGGGTATTAGTATATCTAATACTAAATTTAAATGTGAAAAACTGTCCTCTAAAAATGGAAATATTGAATGAATTGATCGTAAATTCTGCAATTTTACTATATTTTTCTTTTTCTCTTCTAGACAAGGTATTAATCGTAGAGAAAATGGAATTTCCACAATAAAAGCAAGCCCCTCTGATATGATTTCAGAATACCAACTTTTGGTGCACATCAAAAATGGAGTTTGATTAGAAGCATTAGAAGAAATAAAAAAATGATTCTGTTGATACATTCGAATAATTAATCGTTTCACAATCAGTAAACTGAATTTATTGTCATAACCTAAACTTTCCGAAGAAATAAAAATAGATCTACCGAAACTACGATCATGAGCAAATGAATAAATATACTCTTGAAAAATAAGTGGATATAGGAAACGGTGTTGTTGATATTTTTCTAGCTGTAAATATTTTAGGATTTCCTTCATTTGAAATTTTAATCAAAAGTAGAAAATTTTTTGGGTTATCAAATGATACATAGTACGATATAGTCAAAACAAGCTATTCTAGTCAGAATAGATACCTCGTAGACAGGTAAAATTATCAACAGATTCTCTACCCTCTCCTTATTCCTATTCATTTACTTTCATTCGTCTATGTTATAGGATAAACAAGATGTTTAGAAATCTTTTATTTTATAAACCTAATCGCTCTTTTGATTTAGGAAAAACTTTTTTAATCAATATACTGCTTCTTTTACACACGTATTTTCATTCCATACTAAAGAATGTTAATAGTTAGGATTCATTAAAAAATATAGATCCACTCATGGGGAAAAAGTCTTTCCCGTATCAGGCACTAATTTATTTTTAACGTCTAATTAGATCGGTAAATTATTCAAATTAAGAATAAAAGCTGGTTGCTTTTTATTTCTAATAATGATTGAAGCCCTGGGGCCTTATCCGTCTATTCATCCGACCAAACTTTATTTTGTTCCGTTGCAAGAATTCAAAAAGATTTTATACCAATCCTAGAGAAATAAAATATCCTCAAAACTCTCTATTGATACGACATGCTATTTTTTCCATTTATTCCCTTTTATGGATCAGTCGTGGTCTTACAAACTAATGGTATGGACGAATTTTTCACTTCACCAAATGTGTAAAAGATTATAGTCGCACTTAAAAGCCGAGTACTCTACCGTTGAGTTAGCAACCCGAATAAAATAGAGATTAAATAAAACTTCAAATAAAAACTAAAGGATGTATAGATACAATCGATCAAAATAAATTAAATTTAAATAAAGAAAAAGAAGATTCGACGAGCTA"
Viscum_articulatum = "GCGAACAACGGGAATTGAACCCGTGCATGGTAGATTCACAATCCACTGCCTTGAACCACTTGGCTATATCCGCCCTCTGTATGTAGTATTTGACTTATAAAAAATTTTTTATAAGTCAAATACATATTCTTTCAAATTAATAAAATATTATTTATAAAGAAAAAAAAAAGAGATCTAATAGTATCTCAAAAAAAATAAAAATGTTTTATCCATTTGTGGATGGAATTTCAACAGCAGCTAAATCTAGAGGAAAGTTATGAGCATTACGTTCATGCATAACTTCCATACCCAAGTTAGCACGATTAATAATATCTGCCCAGGTATTAATGATACGACCTTGACTATCAACTATAGATTGGTTGAAATTGAAACCATTTAAGTTAAAAGCCATGGTACTTATACCTAAAGCAGTGAACCAGATACCTACAACAGGCCAAGCAGCAAGGAAGAAATGTAAGGAACGAGAATTGTTGAAACTAGCATATTGGAAGATCAATCGTCCAAAATAACCATGAGCAGCTACGATATTATAAGTTTCTTCTTCTTGACCAAATATGTAACCTGCATTAGCAGATTCATTTTCTGTAGTTTCCCTGATCAAACTAGAGGTTACCAAAGAACCATGCATAGCACTGAATAGAGAGCCGCCAAATACACCAGCAACGCCTAACATATGAAACGGGTGCATAAGGATGTTGTGCTCGGCCTGGAATACAATCATGAAGTTAAAAGTACCAGATATTCCTAGAGGCATACCATCAGAAAAACTTCCTTGCCCGATTGGATAGATCAAAAAAACAGCAGTTGCTGCTGCTACAGGAGCTGAATATGCAACAGCAATCCAAGGACGCATCCCCAGACGGAAGCTCAGTTCCCACTCACGACCCATGTAAAAAGCTACACCAAGTAAGAAGTGTAGAACAATAAACTCATAAGGACCACCATTGTATAACCATTCATCAACTGAAGCAGCTTCCCATATCGGATAAAAATGCAAACCAATCGCTGCCGAAGTCGGAATAATGGCACCAGAAATAATATTGTTTCCATAAAGTAGAGATCCAGATACTGGTTCACGAATACCATCAATATCGACTGAAGGAGCAGCAAGAAAGGCAATTAGAAATACAGAAGTTGCGGTCAATAGGCTAGGGATCATCAAAACACCAAACCATCCAATGTAAAGGCGGTTTTCAGTGCTGGTTATCCAGTTACAGAAGCGACCCCATAGGGTTTCGTTTTCTCGTCTCTCTAAAATGGCAGTCATAGTCTATTTTTTTTTTGCTTGATTGATCATCAGGGACTCCCAAGCAAAGGAATGTATTTTTTTTTTTGAGTAAATAAACATTCATGTGTCTTGTTATTAAACAGTATAACATGACTTATATAGTCATGTCAACCAATTAATAATTTTATAGAATAGTCAATCCATCAACTTGTACAAAAGAACAAGGGAAATAAAAAAACGAGAAAATATTGAATAAAAAATATCATCATATAATGGGTTGCCCGGGACTCGAACCCGGAACTAGTCGGATGGAGTCGAATTTCCCCTTGTAAAACGAAATGAAAGACATTACAAAAAACAAAATATGAATTAACACAAAAAATCCCTCCCTAAACCGTGCTTGCTTATTTCATTGCACACGGCTTTCCCTATGTATTATAGTCCGTTCTGTCCTCAAGTCGGAACTTAAAATAAAAAAAATAGTTGATTCACTAATATTAGTTAGTCTGCATGAACTATTCATAATAGAACGGAATTTTCTTTTCATATCACATTGAAAAGTCATTTTCAATTACATGATTTGAAAACCAATCAGTGGATGAAGAATGATGGATCAGATCATTAATACAAAGAATATCCAAATACCAAATCCGTCTTATACTCTTCCTATATAAGAATAACCTTCGCGAAGTATAAGATCTTGAAAGAATGAAAGAAATAACTTGTGCGTCCTCCGTAACAAAATCTTCCAAAAATGCCGAACCGAATTTATTCAAAAACGCACGTACAGTAGATTTGTGTTTACGAGCGAGAGTTCTAACACAAGAAAGTTGAAGAATATACTTTATTCGAAAAATAATTTTTTTTTTTGAGGATCCGCTGTGATAATGAGAAAGATTTCTGCGTATAAACCAAAATAGGTCAAAAATATCCGAATCCGATAAATCAGACCAGACCGACTTACTTATGGGATGTCCTAAGACATTACAAAATTTTTTTTTCGCGAATGATCTCATCAAAGGAAGAATAGGAACTGTGGTATCACACTTATTTGTTATACCATTGTCAATGATATATGAATTTTCGATCATTTGACTCCGACCCAGTGAAATATTGAGTCGTACACTTGAAAGATAGCCTAGAAAGTAGAGTGAAGTATTCGCTATATTCTTATGGATCCTTGGTTGAGGAGACCACACATAAAAACGACATTGCCAGAAATTCATAAGGTAATATTTCCATTTATTCATCAGAATAGGCTTCCCTTTTGAAGCCAGAATGGATTTTCTTTGATATCTAACATAATGCATGAAAGGATCCTTGAACAACCATAACATGGTCTGAAAATGTGATGAAGTAAAGAGAGCTACGAGATGTTCTATTTTGCCATAGAAATAGATTCTATCAAAAAGGGTTACAAAAAATGTTGATCGTAAATGAGATTGGTTACGGAGAAAAACGAAAATAGATTCGTATTCAAAGACATGAGAATTATATAAGAACAAGAGCAATCTTTTATTTTTTTTTGAAAGTGAAATGGATCTATTTGGATAAATCAAAGGATTCCATTTCAAATTTTCTTGGAAAAAAAAAAATCGTAATAAATGCAAAGAAGAGGAATCTTTGACCCAGTAACGAAGAATTTGAACCAAGATTTCCAGATGGATAGGATAGGGTATAAGTATATTTGAAAAAAAAATTAAATGTGAAAA"
Orobanche_rapum_genistae = "TTTATATACTATAAATTAAAATTAAAACATAAAATGTAAGACTTGTTATTCAACAGTAATGACTTATATATTCGTGTCAACAAATCTCAATAACTATATTAAATATATTCAAGCGGATTACAAAAAGAAAATATGGATCATAGAATTTATAATTTTAATATGACGGTGGGTTGCCCGGGATTCGAACCCGGAACTAATCGGATGGAGTAGATAATTTGTTTGTTATGTTAGTTAAATAAAGAAAAATCTCTCCCCAAGCCGTGCTTGCAGTTTTCACTGCACACGGCTTTCCCTATGTATACATAATTTTCCGTTCTTATAATAAATAAATAAACTTTATTTAAATCAATTGAATATTCAATTGATTTAACCCTTATTACATATTACATACTATATAAACATTTCAGAATAGTATAAATCCATGAATAAATTTTATTTTCAAAATTTCATTATTTGTAATAGGCCATAATAAAAACAATATCCAAATACCAAATTCGACTTCTATATACTTCCTGTAAACTGGAAGAAGCTTTTGGTAATGTCAAAAAAAGAACGTTTTCTTTCGCCATAAGAAATTCTTCTAATAATTCCGAGTCAAATCTTTTCAAAAAAGTACGTAGAGTACTTTTGTGTTTCCGAGCCAAAGTTTTAGCACAAGAAAGTTGAAGTATATACTTTATTCGATACAAACTTTTTTTTTTTGAAGATCCACTATGATAATGATAAAAATTTCTGCATATAGACCCAAATCGATCAATAATATTAGAATCTGATAAATTAGCCCAAACTGACTTACTAATGGGATGCCCTAATACGTTACAAAATTTCGCTTTAGCCAATGAAGCAATCAAAGGAATAATTGGAACAAAGGTATCGACTTTATTAATAGCATTATTTATTAGAAATGAATTTTCTAGGATTTTACTCCGTATTACTGAAGAGTTCATTCGCAAGTTTAAAAGATAACCTAAAAATTCAAAGGACTGATTGGATAATTGGTTTATATAAATCCTTCTTGTATAAAACCACAGAGAAAAATGCCATTGCCAAAAAGTAATCAAGTACAATTTCCATTTATTCATGAAAAAGGGCGTCCCTTTTGAAGCCAGAATGGATTTTCTTTGATACCTAATATAATGAAAGCAAGGTTCCTTGAACACCCATTGGTTCACTTGAAAATCCTTAACCTTTACAAAAACATTCACAAGATATTTTATTTTTCCATAGAAATATATTCGTTCAAGAAGAACTCCAAAGGATATTGATCGTAAATGATAAGATTGGTTACGTAGAAAGACGAAAATATATTCGTATTCACATACATGAGAATTATATAAGAATAAGAATAATCTTTGATTACTTTTTGCAAAAAAAGAACTGGCTTTCTTTGGAGCAATAAAACTATTCCCATTTTTGTTGATAAAGAATCGTAATAAATGCAAAGAAGAGGCATCTTTTATCCAATATCGAAGAGTTTGGACCAATATTTCCGCATGGACCAAGTGGGGTATTTGTATATCTAATAGTAAATTTAAATGTGAAAGACTATCCTCTAAAAATGGAAATATTGAATGAATTGATCGTAAATTCTGCGATTTTACTATCTTTTTATTTTTCTCTTCTATACAAGATATTAATCGTAGAGAAAATGGAATTTCCACAATAAAAGCAAGCCCCTCTGATATGATTTCAGAATACCAACTTTTGGTGCGCATCAAAAATGGAGTTTGATTAGAAGCATTAGAAGAAATAAAAAAATGATTCTGTTGATACATTCGAGTAATTAATCGTTTCACAATCAGTAAACTGGATTTCTTGTCATAACCTAAACTTTCCGAATAAATAAAAATAGATCTACCGAAACCACGATCATGAGCAAATGAATAAATATACTCCTGAAAAATAAGTGGATATAGGAAACGGTGTTGTTGAGATCTTTCTAGCTGTAAATATTTTTGGATTTCCTCCATTTGAAATTTAAATCAAAAGTAGAAAATTTTGTGGGTTATCAAATGATACATAGTACGATATAGTCAAAACAAACTATTCTAGTCAGAATAGATACCTCGTAGACAGGTATCAACAGACTCTCTACCCTCCCCTTATTCCTATTCATTTATTTCATTCGTCTATGTTATAGGATAAACAAGATGTTTAGAAATCTTTTATTTTATAAACCTAATCGCTCTTTTGATTTAGGAAAAACTTTTTTAATCAATATACTGCTTCTTTTACACACGCATTTTCATTTCATACTAGAGAATGTTAATAGTTAGGATTCATTAAAAAATATAGATCCACTCGTGGGGGAGAAGTCCTTCCCGTATCAGGCACTAATCTATTTTTAACGTCTAATTAGATCGGTAAATTATTCAAATTAAGAATAGAAGCTGGTTGCTTTTTATTTCTAATAATGAATTGAAGCCCTGGGGCCTTATCCATCTATTCATCCGACCCAAACTTTATTTTGTTCCGTTGCAAGAATTCAAACAAGATTTTATACTAATCCTAGAGGAATCAAATATCCTCAAAACTCTCCATTGATACGACATGCTATTTTTTCCATTTATTCCCTTTTACGGATCAGTCGTGGTTTTACAAACTAATGGTATGGACGAATTCTTCACTTCATCAAATGTGTAAAAGATTATAGTCGCACTTAAAAGCCGAGTACTCTACCGTTGAGTTAGCAACCCGAATAAAATAGAGATTAAACAAAACTTCAAATAAAAACTAAAGGATGTATAGATACAATCGATCAAAATAAATTAAATTTAAACAAAGAGAAAGAAGATTCGACGAGCTAATAAAATAAAATGCTAAGCTAATAAATCTACAAAAACAGGTTTTCTAAAAGATTCGAAACATCGTTACAATGAAAACTACATACATAATTTAAGGAAATGTCTAAATTTGATATTTATAAGATCAATATATACT"
Cumathamnion_serrulatum = "ATAAATGTCTAATTCTGTAGAAGAACGGACAAGAATTAAAAATGAGCGTTATGAATCAGGTGTAATTCCATATGCAAAAATGGGATACTGGGATCCAAACTATGTAATTAAAGAAACTGATGTATTATCATTATTTCGTGTTACTCCACAACCAGGTGTCGATCCAGTAGAAGCATCTGCAGCTGTTGCAGGTGAGTCATCTACGGCTACATGGACTGTAGTATGGACTGATTTATTAACTGCTTGTGATTTATACCGTGCAAAAGCTTACAAAGTTGATGCAGTTCCTAATACATCTGATCAGTATTTTGCATATATTGCTTATGACATTGATCTATTTGAAGAAGGATCTATTGCTAATTTGACAGCTTCTATTATTGGTAATGTATTTGGTTTTAAAGCAGTAAAAGCATTACGATTAGAAGATATGCGTATGCCAGTAGCTTACCTAAAAACATTCCAAGGCCCTGCAACAGGTATTATTGTAGAACGTGAACGAATGGATAAATTTGGTCGTCCATTTTTAGGCGCAACAGTGAAACCTAAGCTAGGTTTATCTGGGAAAAACTATGGACGCGTAGTTTATGAAGGATTAAAAGGTGGACTAGATTTCTTAAAAGATGATGAAAATATCAACTCTCAACCATTCATGCGTTGGAAAGAGAGATTCTTATATTCAATGGAAGCTGTAAATCGTTCAATTGCCGCTAGTGGTGAAGTAAAAGGTCACTACATGAATGTTACAGCAGCTACTATGGAAAACATGTATGAAAGAGCTGAATTTGCTAAAGATTTAGGTACAGTTATTATCATGGTTGACCTTGTAATTGGATATACTGCTATTCAATCAATGGCAATTTGGTCTCGTAAAAATGATATGATTTTACACTTACATCGTGCAGGTAATTCAACATATTCTCGTCAAAAAATTCATGGTATGAATTTCAGGGTTATTTGTAAATGGATGCGTATGGCAGGTGTTGATCATATTCATGCAGGTACAGTAGTAGGTAAATTAGAAGGTGATCCTTTAATGATCAGAGGCTTCTATAACACATTATTATTACCATACCTAGAAACTAATTTACCTCAAGGTATATTTTTTCAACAAGATTGGGCAGCATTACGTAAAGTAACGCCTGTTGCCTCAGGTGGTATTCATTGTGGACAAATGCATCAATTATTAGATTATCTTGGAAATGATGTAGTACTTCAATTTGGAGGAGGTACTATTGGACATCCAGATGGTATTCAAGCAGGTGCAACAGCTAACCGTGTAGCTTTAGAATCTATGGTAATCGCGAGAAATGAAATGCGTGATTATGTAGCAGAAGGGCCACAAATTCTGCGTGATGCAGCAAAAACATGTGGGCCTCTACAAACAGCATTAGATTTATGGAAAGATATTTCATTTAACTATACTTCTACAGATACAGCTGACTTTGTAGAAACTCCAACAGCTAATGTTTAATACTATAAAATAAAAATAAATTGATCACAGTCCAATATATAGAAATTGTTATTAGTGATTCATTAACCTTCATAAGGAGTATAAAATAGTGAGACTTACACAAGGAACTTTTTCCTTCTTACCAGACCTAACTGACGAACAAATTAAAAAGCAAATTGAATATGCAATGTCTCAAAAATGGGCTATTAATATTGAATTTACAGAAGATCCACATCCAAGAAATAATTTTTGGGAATTATGGGGACTTCCATTATTTGATCTTAAAGACGCTAGTACAGTTATGTATGAAATGAATAGTTGCCGTCAACAAAATTCAAATAAATATATCAAAGTAAACGCTTTTGATAATGCAAGAGGCGTTGAAAGTTGTGTTTTATCATTTCTTGTTAATAGACCTTCATTCGAGCCTGGCTTTGAGTTAGTAAGAACAGAAGATGTAGGAAGAAACCAAAAATACTGTTTCCGTAGTTATGCTACAGAAAAACCAGAAGGTTCTCGATATTAAATTTTATCATAGATAAGATTATTTAACTTAAAAATATAAAATCAAAAAAATAAAAATTTATTTTTTTGATTTTTAAATAATAAATTTTTGAAACAATTATATAATGACTCTAAACTATTCAGATGATACTCTAGTAAATTTACAAGAAGAATATGATAAAACAAAAATTCAAGAAGTAATAGATGAACTAGAGCAAGAATTAGTAGGCTTAACACCCGTAAAAACACGCATCAAAGAGATCGCCGCCCTTTTATTAATTGATAGATTAAGAAACAATTTAGGCTTAGTCTCTGGAAACCCTGGATTACATATGTCTTTTACAGGAAGCCCTGGGACAGGAAAAACAACTGTAGCAATGAAGATGGCAGATATTCTACATAGATTAGGATATATTAGAAAAGGGCATTTATTGACTGTTACTAGGGATGATCTTGTTGGACAGTATATTGGACATACTGCTCCTAAAACTAAAGAAGTATTAAAACGAGCAATGGGAGGTGTTTTATTTATTGATGAGGCTTATTATCTTTATAAGCCTGATAATGAACGAGATTATGGAGCAGAAGCCATAGAAATTTTATTACAAGTTATGGAAAATCAAAGAGATGATATTGTTGTAATATTTGCTGGCTATAAAGATAAAATGGACAAATTTTATGAATCAAATCCTGGTCTATCTTCACGTGTGACTAATCATGTAGATTTTCCTGATTATACTGCTGAAGAATTGTTGCAAATCGCAAAATTAATGTTAGAAGAACAACAATATCAATTTGCAATAAATGCTGATACGGTGTTATTAGAATATGCTGAAAGAAGAATGAAACAACCTCATTTTGCAAATGCTAGAAGTATAAAGAATGCTATTGATAGAGCAAGAATGAGACAAGCAAATAGAATATTTATCAGTGGTGATAAAATTTTAACTAAAAGTGATCTTGTGACAATTGAATCGGAAGATATT"
# Arabidopsis_thaliana = ""
# Cuscuta_gronovii = "CGACGGGAATTGAACCCGCGCATAGTGGATTCACAATCCACTGCCTTCATCCACTTGGCTACATCCGCCCCAAAAAAAAATGAAAAACTGGAGCAATCCTGCCTGAAAAGCAAGGATTGTTCCAGTTTTTCATTTTTGATAATAAGACCTCTAATCCTTATCTCATCTTACGCGTTTGTAGCTGAAACTTCAAAAGTAGCTAGATCTAAAGGAAAGTTGTGCGCATTACGCTCATGCATAACTTCCATCCCAAGATTGGCACGATTTATGATATCAGCCCAAGTATTAATTACATGGCCTTTACTATCCACTACAGACTGGTTGAAATTAAATCCATTTAGGTTGAATGCCATGGTGCTTATACCTAAAGCAGTGAACCAGATACCTATAACAGGCCAAGCAGCTAAAAAGAAATGTAACGAACGAGAATTGTTGAAACTTGCGTATTGGAAAATCAATCGGCCAAAATAACCATGAGCGGCTACAATATTATAAGTTTCTTCTTCTTGACCAAATTTGTAACCTTTGTTAGCCGATTCACTTTCGGTAGTTTCCCTAATTAAACTAGAAGTTACCAAGGAGCCATGCATAGCACTGAATAGGGAGCCTCCAAATACACCAGCGACACCTAACATATGAAATGGGTGCATAAGAATGTTGTGCTCAGCCTGGAATACTATCATGAAATTGAACGTACCAGAGATTCCCAAGGGCATCCCATCAGAAAAACTCCCTTGACCAATTGGATAGATCAAGAAAACGGCGGTAGCAGCTGCAACAGGAGCTGAATACGCAATAGCAATCCATGGGCGCATACCCAAGCGGAAACTAAGTTCCCACTCGCGGCCCATATAACATGCTACACCAAGTAAAAAATGTAGAACGATGAGTTCATAAGGACCACCATTGTATAACCATTCAGCGATGGATGCTGCTTCCCATATTGGATAAAAGTGCAACCCTATAGCTGCAGAAGTCGGAATAATAGCACCTGAAATGATATTATTTCCATAAAGTAGAGATCCAGAAACAGGTTCACGAATACCATCAATATCTACAGGAGGCGCAGCAATGAAAGCAATAAGAAATACAGAAGTTGCGGTCAACAAAGTAGGGATCATCAACACACCAAACCATCCAATATAAAGACGATTTTCAGTGCTGGTTATCCAATTACAGAAACGACCCCATAAGTTTTCGCTCTTGCGTCTATCTAAAACTACAGTCACAGTAATTTATTAAGTATATTTAATGATCAGGAACTCCCAAGCATATGAAAAAAATAGAACTGAAGAACGCTTGTTATTTTATGATATATAATATGTTCCAATTGATATCGATAATTTGAGAAAAAGCTAAAGCTACGACTAAAATTTTAGTGGAATCGGTATATTTGAACCCGGATTCCGGATTAAAGTAAACAATGGATTAAATAAAAACCCCGGTTCGTACATCATACACGTTACGTTTACTCTTATCCTACATGGTAATTTTAATTTATATGGTGTAGACTTTATTTTTTAACAAAAAATTTAAAGTGGAAAACTTACTTTTTATTAAATTTATTTCTTTAGATCAAAATATCATAACCAAGAGAAATTTCCATGGTAAACATTTAGGATGCAAAAACTTGGATAAATCTAATCCGCTTTTTTTAAAAACGTCCTAAATTGGATTATCTCTATCTCATTACCTTGAAACTGACGGAATCTTCCGATTGGACCGTGACACGAACACCCGTTTTCCCATCCAAAAACAGATTGACGATAAATCTATGATTGATGTTATTTGTCTACAAACATATGTTTTATGACATTTTTTATAAATTTTATTAAGAAAAATAAATAAATAGCAATTATTTATTTTTCTTAATAAAATTTATAATGAGAAAAAGATCTGGGACGGAAGGATTCGAACCTACGAATAGCGGGACCAAAACCCGTTGCCTTACCCCTTGGCCACGCCCCATAGTCCAAAAAGTACAATGAAAATAATTATTTTGTGATTTTGAATTAAATATCACTGAAATGACATCCCTATTTAAAATCAAAATTATAGAATACCCTCTATGCAAGTAGATTGAATAATTCGTGTATTTTTTCAGTGGAGAAATTTTTAGGTAGCACTGCAAGGAATTTATTAATTGATATAATATTATTCATTTACCATTGTATTTAAAATCTTAATTTTTGCAATATTTTCTAGATGTGGGACTTAAAATAAAACGAACACTTTAAGTCTTTTTGGTCCCCCCACAGTTATTTATTTTCATTAATCTGAAATATCAAAGCAGTCATCTCCAATAAAAAAATGCTTAATTTTATTAGTATTATTTGTATTGATTCTGTCCTGTATTCGAATAGTTTATTCTTCAGCAAATTGCCCGAAGCCTATTCTTTTTTAACTCCACTCGTAAATTTTATGCCGGTCATACCTGTGCTCTTTTTTCTCTTCGCATTTGTTTGGCAGGCTGCTGTCAGTTTTCGTTGAAATTTTACAGAAATATGAATTAAGTAAACTTTTATAGTCTTCACTTTAATTGAAACCTTATTCTGGCTGCTTTCTGAAAAAACCTTACTAGGATTTGGGTTACTTACACTATAAACGATATAAAAATTAGGAAAACTTTTACCTAAAATTACTACATTCAATTATTTTTGGAGAGATGACTTTATTTCGTATTACCAAACCCGGATTGGATTGATGGTCCAAAAATCGCGAATATAGTCCATATTTTTTTTAAGAAACCAAGGTATATTTGTAATGTTTATTCTAAAACTCTTCGTGTACACCGTTGTTATCTTTTTTGTTTCTCTATTTATCTTTGGGTTCCTCTCTAATGATCCAAGACGCAATCCCGAACCTGAAGAAGACTAAATATCCATTTTTGCAAATTATTTAATTTGCAAAAATGGAAAGAGAGGGATTCGAACCCTCGGT"
# Nuytsia_floribunda = "GTGGATTCACAATCCACTGCCTTGATCCACTTGGCTACATCCACCCTTCATTTACTAACTATTTATACCATTCAAAATTTTTCTATTGCATAAAACTTTATATATTTTTTATTTTTATATTTATTAGAATAAGTAGAATAAGATTCATTATAATTCTAATAAGAATAATGGAATTCTTTTATCTTATCTATTTTATTCCGTTCCGAAATTCACACAAGTAAAATATTTACTCATAAACCAACCAATAAGATAAGAATGGATTAAAACAACTTTAAAACAACTTCTGAGAGTAAAAAAGAGTGATAAGTAAAGAAGCAATATCAACCCTCTTGATATTGCTTCTTTACTTTCAAAAACTCATATACCCTAAGACGGAAATCTTATCCATTTGTAGACAGAACTTCAACAGCAGCTAAATCTAAAGGAAAGTTATGAGCATTACGTTCATGCATAACTTCCATACCAAGGTTGGCACGGTTAATGATATCGGCCCAAGTATTAATTACACGACCCTGACTATCAACTACAGATTGGTTGAAATTAAAACCGTTTAAGTTGAAAGCCATGGTGCTAATACCTAAGGCTGTGAACCAGATACCCACTACAGGCCAAGCCGCTAGAAAGAAATGTAAAGAACGAGAATTGTTGAAACTAGCATATTGGAAAATCAATCGGCCAAAATAACCATGAGCGGCTACGATGTTATAAGTTTCTTCTTCTTGACCGAATCTGTAACCCGCATTAGCGGATTGATTTTCTGTAGTTTCCCTGATCAAACTAGAGGTTACCAAAGAACCATGCATAGCACTGAATAGAGAGCCGCCGAATACACCAGCTACGCCTAACATGTGAAAAGGATGCATAAGAATGTTGTGCTCAGCCTGGAATACAATCATGAAGTTAAAAGTACCAGAAATTCCTAGGGGCATACCATCGGAAAAACTTCCTTGACCAATTGGGTAGATCAAGAAAACAGCGGTAGCCGCTGCAACAGGAGCTGAATATGCAACAGCAATCCAAGGACGCATACCCAGACGGAAGCTAAGTTCCCACTCACGACCCATGTAACAAGCTACACCAAGTAAAAAGTGTAGAACAATTAGCTCATAAGGACCACCGTTGTATAACCATTCATCAACGGATGCAGCTTCCCATATCGGGTAAAAATGTAAACCTATAGCTGCAGACGTAGGAATAATGGCACCAGAGATAATATTGTTTCCATAAAGTAGAGATCCAGAAACGGGTTCACGAATACCATCAATATCTACTGGCGGAGCAGCAATGAAGGCAATAATAAATACAGAAGTTGCAGTCAATAGGGTAGGTATCATCAAAACCCCAAACCATCCAATGTAAAGGCGGTTTTCGGTGCTGGTTACCCAGTTACAGAAACGACCCCATAGGCTTTCGCTTTCGCGTCTCTCTAAAATTGCAGTCATGGTAAAATCTTGGTTTATTTAATCATCAGAGACTCCCAAGCACGAGAACTCTCTATTATTATTTATTATTAGTATTAGTTTATTAGAGAATTGATAGATTATAATTATAAATTATAGAGAATTGAAAGCTTGTTATTCAACAGTATAACATAACTTATATGCCCTTGTCAACCAATATCAACATCCATAAAAAGTTATCTATTATAATAGCTATCTATTATCCACCCGGACCCCGTAAGAATTCTTTGTGAATGGCTAAAGTAAAAAAAACGAATGGAATAGTATTTCAATATGATAATGGGTTGCCCGGGACTTGAACCCGGAACCAGTCGGATGGAGTAGATAATTTCCTTGTTAACGTGCTAAATTATCAATAAGATAAATAAGAAAAACCCTTCCCCAAACCGCGCTTGCCTTTTTCATTGCACACGGCTTTCCCTATGTATATATTCTTTTAGTGCATAAACTTTTAGTGCATAAACGTTTCATAATAGAACTATTTGTCATCATTTAGGGATAATTTTCAGTTACATGATTTTATAACTAATCATCAATGATTGACTAGATCATTGATACAAATAATATCCAAATACCAAATCCGCTCTTCTCTATATAAACTGCGCGAAGTACAAGAATATCTTGATAAGATCAAAGAAAAAACTTGTTCGTCCTCCGTAAAAAATTCTTCCAAAAATTCTGGACCTAATCTTTTCAAAAAAGCGCGCAGAGTGCTTTTGTGTTTACGAGCTAAAGTTCTAGTACAAGAAAGTCGAAGTATATACTTTATTTGATACAAACTCTTTTTTTTTGAGGCTCCGCTGTAATAATGAGAAAGATTTCTGCATATACGCCAAAATAAGTCAATAATATCATAATCGGATAAATCGGCCCAGACCAACTTACTAATGGGGTGCCCTAAGACGTCACAAACTTTCGCTTTAGCCAACGATCCAACCAAAGGAATAATTGGAACTGTGGTATCAAACGTCTTAATAACATTATTTATTATAAATGAATTTTCTAGCATTTGACTTCGTCCCACTGAAGGGTTTAATCGCATACTTGCACTTGAAAGATAGCCTAGAAAGCCGAGGAAATGCTTGGATAATGTATTTATATGGAGCCTTTCTGGTTGAGACCACACATAAAAACGACATTTCCAAAAAAGGGCAAGGTAATATTTCCATTTATTCAGCAGAAGAGACGTCCGTTTTGAAGCCAGAATGAATTTCCCTTGATACCTAACATAATGCATGAAAGGATCTTTGAACAGCCATGAAATAGCTTGAAAATCCTTAGTAAAGACATTTACGAGATACTCTTTTTTTATTTTTCCATAGAAAAAAATTCGCTCAAAAAGGGTTCCAAGAAATGTTGATCGTAAATGAGAAGATTGGTTACGTAAAAAAACGTAAATGGATTCGTATTCACAGACATGAGAATTATATAAGAATAAGGACAATCTTTGATTTCTTTTTGAAAGGGTGGAAATATATTT"
# Cytinus_hypocistis = "ACATGCTTAGTCCCAAAAAAACTAAATTTCGTAAACAACATAGAGGGAGAATAAAAGGAATATCTTTTCGAGGAAATAATATTTGCTTTGGTAAATATGCTCTTCAAGCACTTGAACCCACTTGGATTACTTCTCGACAAATAGAAGCAGGTCGACGTGCTATAACACGAAATGTACGGCGTGGTGTAAAAATATGGTTACGCATATTTCCAGATAAACCAGTTACATTTAGAGCTCTAGAAACGCGTATGGGTTCGGGTAAAGGAGATCCTGAATATTGGGTAGCTGTTGTTAAACCTGGTAAAATACTGTATGAAATAAATGGAGTAACTGAAATTACAGCCAAAAAAGCTATTTTAATAGCAGCATCAAAATTACCTATAAAAACAAAATTAATTATGTTATAATACCATAACCAAACTCATTATTTTTTTATTTTTTTTATTGAAATATAAAAGTTAAAAATGATTCAATCTCAAACCTATTTAAATGTAGCAGATAACAGTGGGGCTCGAAAATTAATGTGTATTAGAATTATAGGATCTAGTAATCGCCAATATGCTTATATTGGCGACATTATTATTGCTGTAATAAAAGACTCAGTACCAAATACATCTATATATAAATCAGAAATTATTAGAGCTGTTATTGTACGTACTTGTAAGGAACTAAAACGTAATAATGGTATAATAATAAAATATGATGATAATGCTGCAGTTGTTATTGATAAAAAAGGAAATCCAAAAGGTAGTAGAATTTTTGGTGCAATAACTAGAGAACTTAGACAGTTAAATTTCACTAAAATAGTATCATTAGCCCCTGATGTCTTATAATTAAGATACTTAAGATACCTAATACCTAAATAATTAAATTTAAATATTAATGATATTAATTTTAATTTATTACAAATAAATAAAATTTTACTATGAATAAGGATATTATTGCTAATTTAATAACTTCCATACGAAATGCTGACATGAATAGAAAGGAAATAATTAGAATAAAATCAACTACCCTTACTGAAAGCATCATAAAAATACTTTATAAAGAGGGTTTCCTGACAAATATAAGGAAACATAGTGAGGGTAAACATAATTTTTTAGTTTTAACCCTACGACATCGAATAAAAAGTAAAAAACTATATTATAAAAATATTTTAAATTTTAAACAGATTAGTCGACCTGGTTTAAGAATATATTATAGTTATAAAAAAATTCCCGAAATTTTAGGTAATATGATAATTGGAATTATTTCTACCTCGCAAGGTATAATAACGGATAGAGAGGCTCAATCTAAAAGAATAGGTGGAGAACTTCTGTGTTGTATATGGTAATTATCTGAATAAAATTTAGGATTAACTACATGAAAATAAAATCGTCTATTCGTAAAATTTGTAAAAAATGCAAATTAATACGTAGAAAAAAACGAATTTTAGTAATTTGTTCAAACCCAAGACATAAACAACGACAAGGTTAATGTAAAAAATATTTATTTACATTTTATATATTTTACATATTATAATTATATAATTATATGTATATTCATACATTTATATGTATATTCATACATTTATCTTATGACAAAACTTATTAAAACTAAGAGTTCACGTAGAAGGTGGTATCGTAGTTTACATAAAAGTACAAATATAATAGAAAATAAAAAAGGAGCTATTCATATTCAAGCAAGTTTTAACAATACTATTATTACTCTGACAGATATATGTGGTAAAGTAATTTATTGGTCTTCCGCAGGTACTTGTGGATTAAAAAGTGCAAGAAGGAAAACACCCCTTGCTGCAAAAATTGCAACAGAAAATATTATTAGAGCAGTAAAGAATAAGGGTCTGCAACGAATTGAAGTTATGATCAAAGGTACCGGTAATGGCAGAAATGCCGCTATACAAGTTATTCGTAAAAGTGGTTTGTTTTTAAGTATTATACGAGATGTAACTCCTATTCCACATAATGGATGTAGACCTCCTAAAAAAAGACGTTTATAAGGATAATAACTAAAAACTATTTAATATACAATAAAATTAATAATATTAATGTTTTAGAGTTAGAGTATTATATATTAGTATTACATATTACAATACAATTAAAAAAATGCCTGTAGGTGTTCCAAAAGTTCCCAGTATATTTACTAGGGACGACGAAGAAAAAAATATATATGAAGAAGACGAAGAAAATTATGAAGAAGAAAAAAATATATATGAAGAAGACGAAGAAAATTATGAAGAAGAAAAAAAAAAGAAAAAAGAAGAGGTAATGTGGGTTGATCTATATACTCGAGTTCATCAAGAGAGATTAATTTTTTTAGGCCAAGAGCTTACTTATAAACTTGGCAATCAAATTATGGGCCTTATGATATACCTTAGTATAGACGATGAGCATAGAGATCAATTTATGTTTATAAATTCCCCTGGAGGATTGATAGTACCAGGAATAGGTATTTTTGATACTATGCAATATATTCAACCAGAAGTTGTAACAATATGCATGGGATTAGCTGCTTCAATGGGATCTTTTATTCTGCTTGGTGGAGAACTTACCAGACGTCTAGCATTAAACCACGCTAGGATAATGATTCACCAACCTATTTCTTCTTTTTTTGAGGCACCTGCGGTAGACTTTCTCTTAGAAGCCGGAGAATTATTGAAACTTAGAGAAATAGTTGTAGGGGTTTATTCTAGAAGAACAGGTAAGCCAAAATGGCTTATATCTGAAGATATGGAAAGAGATTATTTTATGTCAGCAGACGAGGCTAAAATATATGGAATTGTCGATGATGTAGGAATTTAATTTTAAATATTAAAAATATTATATCATCCGGTTAAGATGGATATAAACCATATATCTTTTATTATGAGTAAGTATGCCAACTATTAAACAGCTTATTAAAAATTCAAGACAGCCACTGAGAAAGATTACAAAATCTCCTGCTCTTAAGAGATGTCCTCAACGTCGAGGAAGATGTCTTAGGCTGTACGTGTGACTCGTTAAGATCATGA"


sequences = [Cuscuta_reflexa, Viscum_coloratum, Cassytha_filiformis, Orobanche_crenata, Orobanche_gracilis, Viscum_articulatum, Orobanche_rapum_genistae, Cumathamnion_serrulatum]

for j in sequences:
    print(dnds(Balanophora_plastid, j))

