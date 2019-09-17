"""
This file contains constants required for peptides and depsipeptides.
Once filled in, the information contained herein should contain all constants
needed to define MS and MSMS fragmentation properties of chosen polymer class
to build MS and MSMS sequence libraries for screening mass spectrometry data

"""

from ..Constants.GlobalChemicalConstants import *

"""
SECTION 1: GENERAL MS1 AND CHEMISTRY RULES
This section should contain the basic information for constructing in silico
MS1 data for polymer class.

MONOMERS = dictionary of monomer one letter codes, along with associated neutral
            monoisotopic masses and reactivity classes (functional groups).
            This dictionary should specify the neutral monoisotopic mass for
            each monomer, its reactive functional groups, and the number of each
            reactive functional group. This information is essential to ensure
            that all theoretical sequences generated are chemically feasible.
            Format =
                    {
                        'X': [
                            mass, [
                                [rxn_class1, n],
                                [rxn_class2, y]
                            ]
                    }
            where X = monomer one letter code; mass = neutral monoisotopic
            mass; rxn_class1 and rxn_class2 = reactivity classes (functional
            groups - e.g. amine, aldehyde); n = number of rxn_class1 functional
            groups; y = number of rxn_class2 functional groups.

MASS_DIFF = the mass difference when adding an additional monomer on to a
            polymer chain (e.g. for condensation polymer = H2O)

ELONGATION_UNIT = the number of additional monomer units typically added when
                elongating a polymer. This will typically be 1 for most polymers

REACTIVITY_CLASSES = dictionary of reactivity classes with associated compatible
                classes and monomers. Format = {'classA' : [['classX', 'classY'],
                                                ['A', 'B']}
                where classA = reaction class, classX and classY = classes
                that are cross-reactive with classA, and A and B are monomers
                within reaction class classA

SYMMETRY = bool to define whether polymer is identical at both ends. Set to false
            for polymers with different termini (e.g. N- and C- termini for peptides),
            true for polymers with identical functional groups at both termini
            in linear chains

CHAIN_TERMINATORS = list of monomers that terminate chain elongation

LOSS_PRODUCTS = dictionary of monomer one letter codes and associated side chain
            neutral loss products, i.e. masses that can be lost from the monomer
            side chain.

IONIZABLE_SIDECHAINS = dictionary of monomers that can be ionised with extra
            adducts at the SIDE CHAIN, with associated adducts, minimum and
            maximum absolute charge states in both positive and negative mode.
            Format: {"X": {"pos": (adduct, a, b), "neg": (adduct, a, b)}} where
            "X" = monomer one letter code, adduct = adduct string (must be found
            in either CATIONS OR ANIONS in GlobalChemicalConstantss), a = min
            side chain charge, b = max side chain charge for ionized form

INTRINSICALLY_CHARGED_MONOMERS = dictionary of monomers that have an intrinsic
            charge (i.e. charged without addition of adducts), with associated
            lists of permissible adducts
"""

MONOMERS = {
    "A": [89.04768, [["amine", 1], ["carboxyl", 1]]],
    "C": [121.01975, [["amine", 1], ["carboxyl", 1]]],
    "D": [133.03752, [["amine", 1], ["carboxyl", 1]]],
    "E": [147.05318, [["amine", 1], ["carboxyl", 1]]],
    "F": [165.07899, [["amine", 1], ["carboxyl", 1]]],
    "G": [75.03204, [["amine", 1], ["carboxyl", 1]]],
    "H": [155.06949, [["amine", 1], ["carboxyl", 1]]],
    "I": [131.09464, [["amine", 1], ["carboxyl", 1]]],
    "K": [146.10554, [["amine", 1], ["carboxyl", 1]]],
    "L": [131.09464, [["amine", 1], ["carboxyl", 1]]],
    "M": [149.05106, [["amine", 1], ["carboxyl", 1]]],
    "N": [132.05351, [["amine", 1], ["carboxyl", 1]]],
    "P": [115.06334, [["amine", 1], ["carboxyl", 1]]],
    "Q": [146.06916, [["amine", 1], ["carboxyl", 1]]],
    "R": [174.11169, [["amine", 1], ["carboxyl", 1]]],
    "S": [105.0426, [["amine", 1], ["carboxyl", 1]]],
    "T": [119.05826, [["amine", 1], ["carboxyl", 1]]],
    "V": [117.07899, [["amine", 1], ["carboxyl", 1]]],
    "W": [204.08989, [["amine", 1], ["carboxyl", 1]]],
    "Y": [181.07391, [["amine", 1], ["carboxyl", 1]]],
    "g": [76.01606, [["hydroxyA", 1], ["carboxyl", 1]]],
    "j": [73.08915, [["amine", 1], ["carboxyl", 1]]],
    "e": [237.10011, [["amine", 1], ["carboxyl", 1]]],
    "k": [243.09510, [["amine", 1], ["carboxyl", 1]]]
}

"""
A = alanine; C = cysteine; D = aspartic acid; E = glutamic acid;
F = phenylalanine; G = glycine; H = histidine; I = isoleucine; K = lysine;
L = leucine; M = methionine; N = asparagine; P = proline; Q = glutamine;
R = arginine; S = serine; T = threonine; V = valine; W = tryptophan;
Y = tyrosine; g = glycolic acid; e = L-glutamic benzyl ester;  
k = Nε-Trifluoroacetyl-L-lysine; j = butyl amine

"""

MASS_DIFF = H2O
ELONGATION_UNIT = 1
REACTIVITY_CLASSES = {
    "amine": [
        ["carboxyl", "hydroxyA"],
        ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q",
         "R", "S", "T", "V", "W", "Y"]
    ],
    "carboxyl": [
        ["amine", "hydroxyA"],
        ["A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q",
        "R", "S", "T", "V", "W", "Y"]
    ],
    "hydroxyA": [
        ["amine", "carboxyl", "hydroxyA"],
        ["g"]
    ]
}
"""
INSERT ADDITIONAL DETAILS REGARDING REACTIVITY CLASSES HERE - FUNCTIONAL GROUPS
AND ANY OTHER RELEVANT DETAILS

"""

SYMMETRY = False
"""
Peptides have two termini - N and C, which terminate in an amine and carboxyl,
respectively

"""

CHAIN_TERMINATORS = []

"""
INSERT ADDITIONAL DETAILS REGARDING CHAIN TERMINATORS HERE

"""

LOSS_PRODUCTS = {
    "S" : [H2O],
    "T": [H2O],
    "E": [H2O],
    "D": [H2O],
    "N" : [NH3, H2O],
    "R": [NH3],
    "K": [NH3],
    "Q" : [NH3],
    "j": [73.08468],
    "e": [108.05751],
    "k": [95.9823]
}
"""
LOSS_PRODUCTS: Side chains with hydroxyl and carboxylic acid groups can lose
H2O; amines can lose NH3; carboxamides can lose H2O and NH3

"""

IONIZABLE_SIDECHAINS = {
    "K": {
        "pos": (H, 1, 1),
        "neg": None},
    "R": {
        "pos": (H, 1, 1),
        "neg": None},
    "E": {
        "pos": None,
        "neg": (-H, 1, 1)},
    "D": {
        "pos": None,
        "neg": (-H, 1, 1)},
    "H": {
        "pos": (H, 1, 1),
        "neg": None}
}

"""
IONIZABLE_SIDECHAINS: Side chains with free amines (K, R, H) can gain a proton
and become cationic; side chains with free carboxylates (E, D) can lose a proton
and become anionic
"""


INTRINSICALLY_CHARGED_MONOMERS = {}

"""
Section 2: MS2 FRAGMENTATION

This section should contain all the information required to construct a basic
MS2 fragment series for linear polymers. Each fragment type is defined as a key
in the FRAG_SERIES dict. Typically, fragment keys are one letter codes used to
denote fragments - e.g. the standard 'b' and 'y' fragment series for peptides.
When building fragment series, the fragment generator will use the following
convention:
                f'{frag}{n}'
frag = fragment one letter code, n = number of monomers in fragment (e.g. b1,
        b2, b3, y1, y2, y3 etc...)

FRAG_SERIES = dictionary of fragment series one letter codes and associated
properties. Each fragment series key = fragment one letter code, value =
subdictionary containing all relevant fragment properties. Below is a list of
fragment properties defined in the FRAG_SERIES dict. This information has been
filled in for the well studied peptide b- and y- fragment series as an example.

Fragment properties:

'terminus' {0 or -1} - specifies which terminus the fragment series starts from.
                    0 = start of sequence, -1 = end of sequence.

'mass_diff' {float} - the difference in mass between the fragment and corresponding
                    subsequence. This may vary depending on whether cations or
                    anions are being fragmented, therefore separate mass_diffs
                    are specified for positive mode ('pos') and negative mode
                    ('neg') mass spec. Example: the 'y3' fragment of peptide
                    sequence 'AGVS' = the mass of (GVS+H) in positive mode, and
                    (GVS-H) in negative mode.

'fragmentation_unit' - the minimum number of monomer units typically added and
                    / or removed at a time when building a fragment series.
                    Default = ELONGATION_UNIT (see Section 1)

'start' - the starting position of the fragment series within the fragmenting
            sequence, relative to the first monomer in the sequence. If this is
            0, fragment series will be generated along the full length of the
            sequence; otherwise it will be generated from 0+n position, where
            n = 'start'

'end' - the ending position of the fragment series within the fragmenting
            sequence, relative to the last monomer in the sequence. If this is
            0, fragment series will be generated along the full length of the
            sequence; otherwise it will be generated up until -(n+1) position,
            where n = 'end'

'intrinsic_adducts' - OPTIONAL. this subdictionary contains any intrinsic
            adducts generated as default for a given fragment series in
            positive and negative mode. Intrinsic adducts are adducts which
            are added to the fragment as default (for example: +H for peptide y
            fragments in positive mode). This information is important when
            adding non-standard adducts (e.g. Na+, K+, Cl- etc..) to MS2
            fragments, as intrinsic adduct masses must be removed when adding
            other adduct masses

'permissible_adducts' - OPTIONAL. this subdictionary contains lists of adducts
            that may be found associated with a particular MS2 fragment series.
            This is to be used only in cases where there are restrictions on
            associated fragments, as otherwise it is assumed that any MS2
            adducts included in the in silico run are compatible with all
            fragment series. Example: peptide b fragments are inherently
            charged as acylium ions, and as they are extremely unlikely to be
            multiply charged in the absence of ionizable or intrinsically
            charged side chains, there are no permissible adducts for this
            series.

MS2_SIGNATURE_IONS = MS2 fragments which can be used as markers for monomers
            and / or small subsequences.
"""

FRAG_SERIES = {

# a and x fragments

    "a": {
        "terminus": 0,
        "mass_diff": {
            "pos": -COOH,
            "neg": None
        },
        "fragmentation_unit": {
            "pos": ELONGATION_UNIT,
            "neg": ELONGATION_UNIT
        },
        "start": 1,
        "end": 0
    },
    "x": {
        "terminus": -1,
        "mass_diff": {
            "pos": -OH + NH3,
            "neg": None
        },
        "fragmentation_unit": {
            "pos": ELONGATION_UNIT,
            "neg": ELONGATION_UNIT
        },
        "start": 1,
        "end": 0
    },


# b and y fragments

    "b": {
        "terminus": 0,
        "mass_diff": {
            "pos": -OH,
            "neg": None
        },
        "fragmentation_unit": {
            "pos": ELONGATION_UNIT,
            "neg": ELONGATION_UNIT
        },
        "start": 0,
        "end": 0,
        "permissible_adducts": {
            "pos": [],
            "neg": []
        }
    },
    "y": {
        "terminus": -1,
        "mass_diff": {
            "pos": +H,
            "neg": -H,
            "exceptions": {
                "pos": {
                    "-1": {"hydroxy_A": -OH}
                }
            }
        },
        "fragmentation_unit": {
            "pos": ELONGATION_UNIT,
            "neg": ELONGATION_UNIT
        },
        "start": 0,
        "end": 0,
        "intrinsic_adducts": {
            "pos": H,
            "neg": -H
        }
    },

# c and z fragments

    "c": {
        "terminus": 0,
        "mass_diff": {
            "pos": -OH + NH3,
            "neg": None
        },
        "fragmentation_unit": {
            "pos": ELONGATION_UNIT,
            "neg": ELONGATION_UNIT
        },
        "start": 0,
        "end": 1
    },
    "z": {
        "terminus": -1,
        "mass_diff": {
            "pos": -NH2,
            "neg": None
        },
        "fragmentation_unit": {
            "pos": ELONGATION_UNIT,
            "neg": ELONGATION_UNIT
        },
        "start": 0,
        "end": 0
    },
}


IMMONIUM_IONS = MS2_SIGNATURE_IONS = {

    "Im": {
        "F": [120.0813], "D": [88.0399], "E": [102.0555],
        "I": [86.0969], "L": [86.0969], "H": [110.0718],
        "C": [76.0221, 133.0436, 134.0276, 147.0772], "K": [101.1079],
        "S": [60.0449], "Y": [136.0762], "V": [72.08133],
        "T": [74.06059], "A": [44.05003], "M": [104.0534, 120.0483],
        "Q": [101.0715], "P": [70.06568], "N": [87.05584], "W": [159.0922],
        "e": [102.0555, 192.10191], "k": [101.1079, 197.08962],

        # 'dominant' is a list of monomers for which the signature ion is
        # expected to be present in all MS2 spectra of a sequence containing
        # the monomer
        
        "dominant": ["F", "I",  "L", "P", "H", "Y"]
        }
}
"""
Amino acids have signature immonium ions in form R=NH2+, where R = amino acid
side chain. These signature ions are unique to each amino acid. Some are found
more commonly than others. Most commonly found immonium ions are included in
the 'dominant' list. For monomers in this list, the corresponding immonium
ion(s) should be found in any MS2 spectrum of a sequence containing that monomer

"""
