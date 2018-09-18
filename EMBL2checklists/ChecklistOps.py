#!/usr/bin/env python2
# -*- coding: utf-8 -*-
'''
Custom operations to generate ENA checklists
'''

#####################
# IMPORT OPERATIONS #
#####################
import Bio
import globalVariables as GlobVars
import MyExceptions as ME

###############
# AUTHOR INFO #
###############
__author__ = 'Michael Gruenstaeudl <m.gruenstaeudl@fu-berlin.de>,\
              Yannick Hartmaring <yanjo@zedat.fu-berlin.de>'
__copyright__ = 'Copyright (C) 2016-2018 Michael Gruenstaeudl'
__info__ = 'EMBL2checklists'
__version__ = '2018.09.17.2300'

#############
# DEBUGGING #
#############
import pdb
# pdb.set_trace()

###########
# CLASSES #
###########
class Writer:
    ''' This class contains functions to write tab-separated
    spreadsheets for submission via the WEBIN checklist submission system.
    Args:
        [specific to function]
    '''

    def __init__(self):
        pass

    def deleteEmptyKeys(self, checklist_type, outp_handle):
        ''' This function delete the not necessary keys
            So the output is dynamical
        Args:
            keys (list)
            outp_handle (list)
        Returns:
            keys (list)
        Raises:
            -
        '''
        keys = GlobVars.GlobalVariables().getQualifiers(checklist_type, 'om')
        toDelete = []
        for i in keys:
            prev = ''
            isEmpty = False
            for j in range(len(outp_handle)):
                try:
                    if prev == outp_handle[j][i]:
                        prev = outp_handle[j][i]
                        isEmpty = True
                    else:
                        isEmpty = False
                        break
                except:
                    isEmpty = True
            if isEmpty:
                toDelete.append(i)
        for delete in toDelete:
            j = 0
            for i in range(len(keys)):
                if keys[j] == delete:
                    del keys[j]
                else:
                    j = j + 1
        return keys

    def writer(self, checklist_type, outp_handle, outp_file):
        ''' This function writes a TSV spreadsheet for submission via
            the WEBIN checklist submission system.
        Args:
            checklist_type (string)
            outp_handle (list)
            outp_file (obj)
        Returns:
            currently nothing; writes string to file
        Raises:
            -
        '''
        translator = GlobVars.GlobalVariables().getTranslator(checklist_type)
        keys = self.deleteEmptyKeys(checklist_type, outp_handle)
        for out_list in outp_handle:
            for key in keys:
                try:
                    out_list[translator[key]] = out_list.pop(key)
                except:
                    pass
        for i in range(len(keys)):
            keys[i] = translator[keys[i]]
        out_string = '\t'.join(keys) + '\n'
        outp_file.write(out_string)
        for out_list in outp_handle:
            out_array = []
            for key in keys:
                    try:
                        out_array.append(out_list[key])
                    except:
                        out_array.append('')
            out_string = '\t'.join(out_array) + '\n'
            outp_file.write(out_string)

class Parser:
    ''' This class contains functions to parse out information from
    sequence records.
    Args:
        -
    '''

    def __init__(self):
        pass

########################################################################
########################################################################


##################################
## PARSING MARKER ABBREVIATIONS ##
##################################
    def parse_marker_abbrevs(self, seq_record, target_qualifiers):
        ''' This function extracts the marker abbreviations from a sequence record.
        Args:
            seq_record (SeqIO)
            target_qualifiers (list)
        Returns:
            marker_abbrev (list)
        Raises:
            DataParsingError: When there are no marker abbreviations it would raise an error
        '''
        gene_qualifiers = [f.qualifiers for f in seq_record.features if not f.type=='source'] # Produces a list of dictionaries
        marker_abbrev = []
        # Extract marker abbreviations
        for keyw in target_qualifiers:
            for dct in gene_qualifiers:
                try:
                    marker_abbrev.extend(dct[keyw])
                except KeyError:
                    marker_abbrev = marker_abbrev
        # Parse raw list of marker abbreviations
        if marker_abbrev:
            # 3.1.1. Extract all unique values in list, keep order of original list
            seen = set()
            marker_abbrev = [elem for elem in marker_abbrev if elem not in seen and not seen.add(elem)]
            # 3.1.2. Remove any multi-word elements
            #marker_abbrev = [elem for elem in marker_abbrev if len(elem.split(" ")) == 1]
        else:
            raise ME.DataParsingError('ERROR: No marker abbreviation parsed successfully for record `%s`' % (seq_record.id))
        return marker_abbrev


########################################################################
########################################################################

##########################
## MANDATORY QUALIFIERS ##
##########################
    def mandatoryQualifiers(self, seq_record, marker_abbrev, counter, checklist_type, env_sample):
        '''fill the mandatory qualifiers for specific checklist_type

        At first it fill the mandatory qualifiers where part of each checklist
        After that it go further for the specific manatory qualifiers and fill the outdict
        with information. It fill the warnings if it cant fill an information to the
        dictionary cause of it is mandatory at all qualifiers have to be filled

        Args:
            -
        Returns:
            outdict (dict) : if information can be filled
            False          : when something went wrong so the main function can skip
                             this seq_record
        Raises:
            it will not raise any errors cause it only give warnings for the specific
            seq_record
        '''

        outdict = GlobVars.GlobalVariables().getOutdict(GlobVars.GlobalVariables().getQualifiers(checklist_type, 'm'))

## CHECKLIST: INTERGENIC SPACER ##
##################################
        if checklist_type == 'IGS':
            # ENTRYNUMBER
            outdict["entrynumber"] = str(counter+1)  # enumerate counter starts counting at 0
            # ORGANISM_NAME
            try:
                outdict["organism"] = [f.qualifiers['organism'] for f in seq_record.features if f.type=='source'][0][0]
            except:
                GlobVars.warnings.append('WARNING: The mandatory source-qualifier ´%s´ is missing from record ´%s´.' % ('organism', seq_record.id))
                return False
            # ENV_SAMPLE
            outdict["env_sample"] = env_sample
            # GENE1 and G1PRESENT
            try:
                try:
                    outdict["gene1"] = [f.qualifiers['gene'] for f in seq_record.features if f.type=='gene'][0][0]
                    outdict["g1present"] = 'yes'
                except:
                    outdict['gene1'] = 'placeholder'
                    outdict["g1present"] = 'no'
            except:
                GlobVars.warnings.append('WARNING: The mandatory feature ´%s´ is missing from record ´%s´.' % ('gene1, g1present', seq_record.id))
                return False
            # GENE2 and G2PRESENT
            try:
                try:
                    outdict["gene2"] = [f.qualifiers['gene'] for f in seq_record.features if f.type=='gene'][1][0]
                    outdict["g2present"] = 'yes'
                except:
                    outdict['gene2'] = 'placeholder'
                    outdict["g2present"] = 'no'
            except:
                GlobVars.warnings.append('WARNING: The mandatory feature ´%s´ is missing from record ´%s´.' % ('gene2, g2present', seq_record.id))
                return False
            # SEQUENCE
            try:
                outdict["sequence"] = str(seq_record.seq)
            except:
                GlobVars.warnings.append('WARNING: The mandatory feature ´%s´ is missing from record ´%s´.' % ('sequence', seq_record.id))
                return False

## CHECKLIST: GENE_INTRON ##
############################
        elif checklist_type == 'gene_intron':
            # ENTRYNUMBER
            outdict["entrynumber"] = str(counter+1)  # enumerate counter starts counting at 0
            # ORGANISM_NAME
            try:
                outdict["organism"] = [f.qualifiers['organism'] for f in seq_record.features if f.type=='source'][0][0]
            except:
                GlobVars.warnings.append('WARNING: The mandatory source-qualifier ´%s´ is missing from record ´%s´.' % ('organism', seq_record.id))
                return False
            # ENV_SAMPLE
            outdict["env_sample"] = env_sample
            # GENE
            try:
                outdict["gene"] = [f.qualifiers['gene'] for f in seq_record.features if f.type=='gene'][0][0]
            except:
                GlobVars.warnings.append('WARNING: The mandatory feature ´%s´ is missing from record ´%s´.' % ('gene', seq_record.id))
                return False
            # INTRON
            try:
                intron = [f for f in seq_record.features if f.type=='intron'][0]
            except:
                GlobVars.warnings.append('WARNING: The mandatory feature ´%s´ is missing from record ´%s´.' % ('intron', seq_record.id))
                return False
            # 5' PARTIAL
            if type(intron.location.start) == Bio.SeqFeature.ExactPosition:
                outdict["fiveprime_partial"] = 'no'
            if type(intron.location.start) == Bio.SeqFeature.BeforePosition:
                outdict["fiveprime_partial"] = 'yes'
            # 3' PARTIAL
            if type(intron.location.end) == Bio.SeqFeature.ExactPosition:
                outdict["threeprime_partial"] = 'no'
            if type(intron.location.end) == Bio.SeqFeature.AfterPosition:
                outdict["threeprime_partial"] = 'yes'
            # 5' INTRON
            outdict["fiveprime_cds"] = str(intron.location.start.position+1)
            # 3' INTRON
            outdict["threeprime_cds"] = str(intron.location.end.position)
            # NUMBER
            try:
                outdict["number"] = [f.qualifiers['number'] for f in seq_record.features if f.type=='intron'][0][0]
            except:
                GlobVars.warnings.append('WARNING: The mandatory feature ´%s´ is missing from record ´%s´.' % ('intron', seq_record.id))
                return False
            # SEQUENCE
            try:
                outdict["sequence"] = str(seq_record.seq)
            except:
                GlobVars.warnings.append('WARNING: The mandatory feature ´%s´ is missing from record ´%s´.' % ('sequence', seq_record.id))
                return False

## CHECKLIST: TRNK_MATK ##
##########################
        elif checklist_type == 'trnK_matK':
            # ENTRYNUMBER
            outdict["entrynumber"] = str(counter+1)  # enumerate counter starts counting at 0
            # ORGANISM_NAME
            try:
                outdict["organism"] = [f.qualifiers['organism'] for f in seq_record.features if f.type=='source'][0][0]
            except:
                GlobVars.warnings.append('WARNING: The mandatory source-qualifier ´%s´ is missing from record ´%s´.' % ('organism', seq_record.id))
                return False
            # trnK_intron
            intron_features, tRNA_features = [], []
            try:
                intron_features_list = sum([f.qualifiers['gene'] for f in seq_record.features if f.type=='intron'], [])
                intron_features = " ".join(intron_features_list)
            except:
                try:
                    tRNA_features_list = sum([f.qualifiers['gene'] for f in seq_record.features if f.type=='tRNA'], [])
                    tRNA_features = " ".join(tRNA_features_list)
                except:
                    GlobVars.warnings.append("WARNING: The mandatory feature combination of ´%s´ is missing from record ´%s´." % ("either an intron feature or a tRNA feature for trnK", seq_record.id))
                    return False
            if 'trnK' in intron_features:
                outdict['trnK_intron_present'] = 'yes'
            elif 'trnK' in tRNA_features:
                outdict['trnK_intron_present'] = 'yes'
            else:
                outdict['trnK_intron_present'] = 'no'
            # matK
            #pdb.set_trace()
            matK_gene = None
            try:
                for gene in [f for f in gene_features if f.type=="gene"]:
                    if "gene" in gene.qualifiers:
                        if 'matK' in gene.qualifiers['gene']:
                            matK_gene = gene
                    if "note" in gene.qualifiers:
                        if 'matK' in gene.qualifiers['note']:
                            matK_gene = gene
            except:
                GlobVars.warnings.append('WARNING: The mandatory feature ´%s´ is missing from record ´%s´.' % ('matK', seq_record.id))
                return False
            # 5'_CDS and 5'_PARTIAL
            # 5'_CDS: Start of the matK coding region relative to the submitted sequence. For a full length CDS this is the position of the first base of the start codon.
            # NOTE: One nucleotide position has to be added to the start position to make it correct.
            outdict["fiveprime_cds"] = str(matK_gene.location.start.position+1)
            # 5'_PARTIAL: cds partial at 5'? (yes/no) For an incomplete CDS with the start codon upstream of the submitted sequence.
            if type(matK_gene.location.start) == Bio.SeqFeature.ExactPosition:
                outdict["fiveprime_partial"] = 'no'
            if type(matK_gene.location.start) == Bio.SeqFeature.BeforePosition:
                outdict["fiveprime_partial"] = 'yes'
            # 3'_CDS and 3'_PARTIAL
            # 3'_CDS: End of the matK coding region relative to the submitted sequence. For a full length CDS this is the position of the last base of the stop codon.
            outdict["threeprime_cds"] = str(matK_gene.location.end.position)
            # 3'_PARTIAL: cds partial at 3'? (yes/no) For an incomplete CDS with the stop codon downstream of the submitted sequence.
            if type(matK_gene.location.end) == Bio.SeqFeature.ExactPosition:
                outdict["threeprime_partial"] = 'no'
            if type(matK_gene.location.end) == Bio.SeqFeature.AfterPosition:
                outdict["threeprime_partial"] = 'yes'
            # SEQUENCE
            try:
                outdict["sequence"] = str(seq_record.seq)
            except:
                GlobVars.warnings.append('WARNING: The mandatory feature ´%s´ is missing from record ´%s´.' % ('sequence', seq_record.id))
                return False

## CHECKLIST: RRNA ##
#####################
        elif checklist_type == 'rRNA':
            # ENTRYNUMBER
            outdict["entrynumber"] = str(counter+1)  # enumerate counter starts counting at 0
            # ORGANISM_NAME
            try:
                outdict["organism"] = [f.qualifiers['organism'] for f in seq_record.features if f.type=='source'][0][0]
            except:
                GlobVars.warnings.append('WARNING: The mandatory source-qualifier ´%s´ is missing from record ´%s´.' % ('organism', seq_record.id))
                return False
            # ENV_SAMPLE
            outdict["env_sample"] = env_sample
            # SEDIMENT
            # sediment can also occur in the qualifiers: sediment, gene and note
            try:
                outdict["sediment"] = [f.qualifiers['product'] for f in seq_record.features if f.type == 'rRNA'][0][0]
            except:
                GlobVars.warnings.append('WARNING: The mandatory feature ´%s´ is missing from record ´%s´.' % ('sediment', seq_record.id))
                return False
            # SEQUENCE
            try:
                outdict["sequence"] = str(seq_record.seq)
            except:
                GlobVars.warnings.append('WARNING: The mandatory feature ´%s´ is missing from record ´%s´.' % ('sequence', seq_record.id))
                return False

## CHECKLIST: ITS ##
####################
        elif checklist_type == 'ITS':
            # ENTRYNUMBER
            outdict["entrynumber"] = str(counter+1)  # enumerate counter starts counting at 0
            # ORGANISM_NAME
            try:
                outdict["organism"] = [f.qualifiers['organism'] for f in seq_record.features if f.type=='source'][0][0]
            except:
                GlobVars.warnings.append('WARNING: The mandatory source-qualifier ´%s´ is missing from record ´%s´.' % ('organism', seq_record.id))
                return False
            # ENV_SAMPLE
            outdict["env_sample"] = env_sample
            # ISOLATION_SOURCE
            if env_sample == 'yes':
                try:
                    outdict["isolation_source"] = [f.qualifiers['isolation_source'] for f in seq_record.features if f.type=='source'][0][0]
                except:
                    GlobVars.warnings.append('WARNING: The mandatory source-qualifier ´%s´ is missing from record ´%s´.' % ('isolation_source', seq_record.id))
                    return False
            ## 18S, 26S/28S
            #try:
            #    rRNA_features_list = sum([f.qualifiers['gene'] for f in seq_record.features if f.type=='rRNA'], [])
            #    rRNA_features = " ".join(rRNA_features_list)
            #    # 18S
            #    if '18S' in rRNA_features:
            #        outdict["RNA_18S"] = 'partial'
            #    else:
            #        outdict["RNA_18S"] = 'no'
            #    # 26S/28S
            #    if '28S' in rRNA_features or '26S' in rRNA_features:
            #        outdict["RNA_28S"] = 'partial'
            #    else:
            #        outdict["RNA_28S"] = 'no'
            #except:
            #    outdict["RNA_18S"] = 'no'
            #    outdict["RNA_28S"] = 'no'
            ## ITS1, ITS2
            #try:
            #    ITS_features_list = sum([f.qualifiers['note'] for f in seq_record.features if f.type=='misc_RNA'], [])
            #    ITS_features = " ".join(ITS_features_list)
            #    # ITS1
            #    if 'ITS1' in ITS_features and '18S' in rRNA_features:
            #        outdict["ITS1_feat"] = 'complete'
            #    else:
            #        outdict["ITS1_feat"] = 'partial'
            #    # ITS2
            #    if 'ITS' in ITS_features and ('28S' in rRNA_features or '26S' in rRNA_features):
            #        outdict["ITS2_feat"] = 'complete'
            #    else:
            #        outdict["ITS2_feat"] = 'partial'
            #except:
            #    GlobVars.warnings.append('WARNING: The mandatory feature combination of ´%s´ in ´%s´ is missing.' % ('either #rRNA for 18S and 26S/28S, or misc_RNA for ITS1 and ITS2', seq_record.id))
            #    return False

            # 18S, 26S/28S, ITS1, ITS2
            rRNA_features, ITS_features = [], []
            try:
                rRNA_features_list = sum([f.qualifiers['gene'] for f in seq_record.features if f.type=='rRNA'], [])
                rRNA_features = " ".join(rRNA_features_list)
            except:
                try:
                    ITS_features_list = sum([f.qualifiers['note'] for f in seq_record.features if f.type=='misc_RNA'], [])
                    ITS_features = " ".join(ITS_features_list)
                except:
                    GlobVars.warnings.append('WARNING: The mandatory feature combination of ´%s´ in ´%s´ is missing.' % ('either rRNA for 18S and 26S/28S, or misc_RNA for ITS1 and ITS2', seq_record.id))
                    return False
            # 18S
            if '18S' in rRNA_features:
                outdict["RNA_18S"] = 'yes'
            else:
                outdict["RNA_18S"] = 'no'
            # 26S/28S
            if '28S' in rRNA_features or '26S' in rRNA_features:
                outdict["RNA_28S"] = 'yes'
            else:
                outdict["RNA_28S"] = 'no'
            # ITS1
            if 'ITS1' in ITS_features or '18S' in rRNA_features:
                outdict["ITS1_feat"] = 'yes'
            else:
                outdict["ITS1_feat"] = 'no'
            # ITS2
            if 'ITS' in ITS_features or ('28S' in rRNA_features or '26S' in rRNA_features):
                outdict["ITS2_feat"] = 'yes'
            else:
                outdict["ITS2_feat"] = 'no'
            # 5.8S # Note: The completeness of the rDNA gene 5.8S is inferred based on the presence of ITS1 and ITS2.
            if '5.8S' in rRNA_features:
                outdict["RNA_58S"] = 'yes'
            elif 'ITS1' in ITS_features and 'ITS2' in ITS_features:
                outdict["RNA_58S"] = 'yes'
            elif '28S' in rRNA_features and '26S' in rRNA_features:
                outdict["RNA_58S"] = 'yes'
            else:
                outdict["RNA_58S"] = 'no'
            # SEQUENCE
            try:
                outdict["sequence"] = str(seq_record.seq)
            except:
                GlobVars.warnings.append('WARNING: The mandatory feature ´%s´ is missing from record ´%s´.' % ('sequence', seq_record.id))
                return False

## CHECKLIST: ETS ##
####################
        elif checklist_type == 'ETS':
            # ENTRYNUMBER
            outdict["entrynumber"] = str(counter+1)  # enumerate counter starts counting at 0
            # ORGANISM_NAME
            try:
                outdict["organism"] = [f.qualifiers['organism'] for f in seq_record.features if f.type=='source'][0][0]
            except:
                GlobVars.warnings.append('WARNING: The mandatory source-qualifier ´%s´ is missing from record ´%s´.' % ('organism', seq_record.id))
                return False

            # Infer ETS type from presence of rRNA
            rRNA_features, ETS_features = [], []
            try:
                rRNA_features_list = sum([f.qualifiers['gene'] for f in seq_record.features if f.type=='rRNA'], [])
                rRNA_features = " ".join(rRNA_features_list)
            except:
                try:
                    ETS_features_list = sum([f.qualifiers['note'] for f in seq_record.features if f.type=='misc_RNA'], [])
                    ETS_features = " ".join(ETS_features_list)
                except:
                    GlobVars.warnings.append("WARNING: The mandatory feature combination of ´%s´ is missing from record ´%s´." % ("either an rRNA feature for 18S or 26S/28S, or a misc_RNA for 5'ETS or 3'ETS", seq_record.id))
                    return False
            # ETS
            if '18S' in rRNA_features:
                outdict["ets_type"] = "5'"
            elif '26S' in rRNA_features or '28S' in rRNA_features:
                outdict["ets_type"] = "3'"
            else:
                if "ETS" in rRNA_features and "5'" in rRNA_features:
                    outdict["ets_type"] = "5'"
                if "ETS" in rRNA_features and "3'" in rRNA_features:
                    outdict["ets_type"] = "3'"
                else:
                    outdict["ets_type"] = "5'"
            # SEQUENCE
            try:
                outdict["sequence"] = str(seq_record.seq)
            except:
                GlobVars.warnings.append('WARNING: The mandatory feature ´%s´ is missing from record ´%s´.' % ('sequence', seq_record.id))
                return False


        return outdict

########################################################################
########################################################################

#########################
## OPTIONAL QUALIFIERS ##
#########################
    def optionalQualifiers(self, seq_record, cl_specific_opt_quals):
        '''fill the optional qualifiers
        Will add all information in the qualifiers to the outdict
        if they are part of the optional qualifiers for the specific checklist_type
        Args:
            seq_record (SeqIO)
            cl_specific_opt_quals (list)
        Returns:
            outdict (dict) : if information can be filled
            False          : when something went wrong so the main function can skip
                             this seq_record
        Raises:
            it will not raise any errors cause it only give warnings for the specific
            seq_record
        '''
        opt_outdict = {}

    # Check if qualifiers in checklist-specific qualifier list
        for i in seq_record.features:
            for j in [q for q in i.qualifiers if q in cl_specific_opt_quals]:
                opt_outdict.update({j:i.qualifiers[j][0]})

    ## PCR PRIMER ##
    ################
        try:
            pcrPrimers = [ i.split(",]") for i in [f.qualifiers['PCR_primers'] for f in seq_record.features if f.type=='source'][0][0].replace(" ","").split(",[") ]
            tmp = []
            for t in pcrPrimers:
                for i in t:
                    tmp.append(i.split(":"))
            pcrPrimers = tmp
            print pcrPrimers
            fwd_name = []
            fwd_seq = []
            rev_name = []
            rev_seq = []
            for i in pcrPrimers:
                if i[0].replace("[","").replace("]","") == 'fwd_name':
                    fwd_name.append(i[1])
                if i[0].replace("[","").replace("]","") == 'fwd_seq':
                    fwd_seq.append(i[1])
                if i[0].replace("[","").replace("]","") == 'rev_name':
                    rev_name.append(i[1])
                if i[0].replace("[","").replace("]","") == 'rev_seq':
                    rev_seq.append(i[1])
            for counter, elem in enumerate(fwd_name):
                opt_outdict.update({'fwd_name'+str(counter+1):elem})
            for counter, elem in enumerate(fwd_seq):
                opt_outdict.update({'fwd_seq'+str(counter+1):elem})
            for counter, elem in enumerate(rev_name):
                opt_outdict.update({'rev_name'+str(counter+1):elem})
            for counter, elem in enumerate(rev_seq):
                opt_outdict.update({'rev_seq'+str(counter+1):elem})
        except:
            pass


        return opt_outdict

########################################################################
########################################################################

