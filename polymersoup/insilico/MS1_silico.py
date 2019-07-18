"""
This file contains functions for generating theoretical MS1 data for ALife
Polymer Data
"""
from .Constants.GlobalChemicalConstants import *
from .Config_files.Depsipeptide_config import *
from .helpers.helpers import *

def __init__():
    """
    Initialises SilicoGenerator and imports constants from polymer config file

    """
    #ADD SOMETHING TO IMPORT CONFIG FILE HERE - IMPORTING DEPSIPEPTIDE
    #CONFIG FILE DIRECTLY IS A TEMPORARY SOLUTION FOR INITIAL TESTING OF
    #FUNCTIONS

def generate_mass_dictionary(
    monomers,
    max_length,
    min_length=1,
    sequencing=True,
    universal_rxn=True,
    chain_terminators=None,
    starting_monomers=None,
    ending_monomers=None):
    """
    [This function takes a list of monomers and outputs a dictionary of all
    possible sequences or compositions that could arise from input monomers
    within the constraints set, along with associated NEUTRAL monoisotopic
    masses]

    Arguments:
        monomers {list} -- [list of monomer one letter codes]
        max_length {int} -- [maximum sequence length (in monomer units)]

    Keyword Arguments:
        min_length {int} -- [minimum sequence length (in monomer units)]
                            (default: {1})
        sequencing {bool} -- [specifies whether all possible sequences are to
                            be enumerated or just compositions. Set to False if
                            you just need to screen for compositions]
                            (default: {True})
        universal_rxn {bool} -- [specifies whether all monomers are universally
                            cross-reactive. If this is set to False, reactivity
                            classes must be read from the polymer config file
                            to ensure that any chemically infeasbile sequences
                            are not included in the final mass dictionary]
                            (default: {True})
        chain_terminators {list} -- [list of monomers which prevent further
                            elongation] (default: {None})
        starting_monomers {list} -- [list of monomers. If this list is input,
                            only sequences beginning with a monomer in this
                            list will be returned] (default: {None})
        ending_monomers {list} -- [list of monomers. If this is input,
                            only sequences ending with a monomer in this list
                            will be returned] (default: {None})

    Returns:
        [massdict] -- [dictionary of sequences and associated neutral
                    monoisotopic masses. Keys = sequence strings, values =
                    masses (float)]
    """

    # check to see if input monomers are set as universally cross-reactive
    # if so, sequence generator used is simpler and (probably) faster
    if universal_rxn:
        sequences = generate_all_sequences(
            monomers,
            max_length,
            min_length,
            sequencing,
            chain_terminators,
            starting_monomers,
            ending_monomers
            )

    # if input monomers are not universally cross-reactive, more complicated
    # function is required to read polymer config file and generate only
    # those sequences that can be produced from appropriately cross-reactive
    # monomers
    elif not universal_rxn:
        sequences = generate_all_sequences_rxn_classes(monomers)

    # work out neutral mass of each sequence and add to mass dictionary in
    # format {seq : mass} where seq = sequence, mass = neutral monoisotopic
    # mass
    massdict = {
        sequence: float("{0:0.4f}".format(find_sequence_mass(sequence)))
        for sequence in sequences
    }

    return massdict

def add_adducts_ms1_massdict(
    massdict,
    adducts,
    mode='pos',
    min_z=1,
    max_z=None
):
    """
    Takes an MS1 mass dictionary of sequences and NEUTRAL MASSES and adds
    charged adducts to sequence masses, giving a list of m/z values for
    each sequence

    Args:
        massdict (dict): dictionary of sequence strings and corresponding
                    neutral masses
        adducts (list): list of adduct string ids - e.g. ['H', 'Na']
        mode (str, optional): specifies whether ions with be cationic or
                    anionic. Use 'pos' and 'neg' for positive and negative
                    modes, respectively. Defaults to 'pos'.
        min_z (int, optional): minimum charge of adduct species. Defaults to 1.
        max_z ([type], optional): maximum charge of adduct species; if None,
                    max charge is determined by maximum charge of
                    adducts specified in GlobalChemicalConstants.
                    Defaults to None.

    Returns:
        adduct_massdict: dictionary of sequences and corresponding m/z values
                    of charged adduct species
    """

    # initiate adduct massdict to be populated with sequences and list of m/z
    # values with adducts
    adduct_massdict = {}

    # iterate through sequences, neutral masses and add adducts to
    # adduct_massdict
    for sequence, neutral_mass in massdict.items():
        adduct_massdict[sequence] = add_adducts_sequence_mass(
            neutral_mass,
            adducts,
            min_z,
            max_z,
            mode
        )

    # return ms1 massdict with charged adducts
    return adduct_massdict

def add_loss_products_ms1_massdict(
    massdict,
    max_total_losses=None
):
    """
    This function takes a dictionary of sequences and corresponding NEUTRAL
    MASSES, and incorporates side chain-specific neutral loss products as
    specified in LOSS_PRODUCTS dict in polymer config file

    Args:
        massdict (dict): dictionary of sequences and corresponding neutral
                        masses
        max_total_losses (int, optional): maximum number of loss products to
                        incorporate per sequence; if None, all possible loss
                        products for a given sequence are incorporated into
                        output loss_product_dict MS1 mass dictionary.
                        Defaults to None.

    Returns:
        loss_product_dict: dictionary of sequences and neutral mass lists with
                        associated side chain-specific neutral loss products
    """

    # initiates dictionary to store sequences with associated neutral loss
    # products
    loss_product_dict = {}

    # iterate through sequences and corresponding neutral masses, adding
    # side chain-specific neutral losses to sequence mass lists
    for sequence, neutral_mass in massdict.items():
        loss_product_dict[sequence] = add_sidechain_neutral_loss_products_sequence(
            sequence,
            neutral_mass,
            max_total_losses
        )

    # return dictionary of sequences and associated lists of neutral masses
    # with neutral loss products
    return loss_product_dict

def generate_ms1_mass_dictionary_adducts_losses(
    monomers,
    max_length,
    adducts,
    mode='pos',
    min_z=1,
    max_z=None,
    losses=True,
    max_total_losses=None,
    loss_product_adducts=None,
    min_length=1,
    chain_terminators=None,
    starting_monomers=None,
    ending_monomers=None,
    universal_rxn=True
):

    # generate neutral mass dictionary of all possible sequences arising from
    # input monomers and constraints set
    MS1_neutral = generate_mass_dictionary(
        monomers,
        max_length,
        min_length,
        True,
        universal_rxn,
        chain_terminators,
        starting_monomers,
        ending_monomers
    )

    # generate a separate mass dictionary, including side chain-specific
    # neutral loss products for every sequence in the MS1_neutral mass
    # dictionary
    MS1_loss_products = add_loss_products_ms1_massdict(
        MS1_neutral,
        max_total_losses
    )
    print(f'max total losses for {monomers} = {max_total_losses}')

    # before adding charged adducts to masses, check whether any specific
    # charged adducts have been specified to add to side chain loss product
    # masses. This is only to be used in cass where the adducts added to loss
    # product masses are to be different to adducts added to full sequence masses
    # Most common usage of this is to add less adducts to loss products in order
    # to minimise false positives in later screening
    if not loss_product_adducts:

        # No specific adducts specified for loss products, so assume all
        # adducts are to be added to all masses and combine both neutral mass
        # dicts + / - loss products
        MS1_neutral = MS1_loss_products

        # add and return charged adducts to MS1 sequence mass lists
        MS1_adduct_dict = add_adducts_ms1_massdict(
            MS1_neutral,
            adducts,
            mode,
            min_z,
            max_z
        )

        # exit function here, returning adduct dict
        return MS1_adduct_dict

    elif loss_product_adducts:
        loss_product_dict = add_adducts_ms1_massdict(
            MS1_loss_products,
            loss_product_adducts,
            mode,
            min_z,
            max_z
        )
        for sequence, masses in loss_product_dict.items():
            MS1_adduct_dict[sequence].extend(
                [
                    mass for mass in masses
                    if mass not in MS1_adduct_dict[sequence]
                ]
            )
    return MS1_adduct_dict
