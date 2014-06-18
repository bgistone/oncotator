"""
By downloading the PROGRAM you agree to the following terms of use:

BROAD INSTITUTE SOFTWARE LICENSE AGREEMENT
FOR ACADEMIC NON-COMMERCIAL RESEARCH PURPOSES ONLY

This Agreement is made between the Broad Institute, Inc. with a principal address at 7 Cambridge Center, Cambridge, MA 02142 ("BROAD") and the LICENSEE and is effective at the date the downloading is completed ("EFFECTIVE DATE").

WHEREAS, LICENSEE desires to license the PROGRAM, as defined hereinafter, and BROAD wishes to have this PROGRAM utilized in the public interest, subject only to the royalty-free, nonexclusive, nontransferable license rights of the United States Government pursuant to 48 CFR 52.227-14; and

WHEREAS, LICENSEE desires to license the PROGRAM and BROAD desires to grant a license on the following terms and conditions.

NOW, THEREFORE, in consideration of the promises and covenants made herein, the parties hereto agree as follows:

1. DEFINITIONS
1.1 "PROGRAM" shall mean the object code and source code known as Oncotator 1.0 and related documentation, if any, as they exist on the EFFECTIVE DATE and can be downloaded from http://www.broadinstitute.org/cancer/cga/oncotator on the EFFECTIVE DATE.  BROAD acknowledges that the PROGRAM employs one or more public domain code(s) that are freely available for public use.

2. LICENSE
2.1   Grant. Subject to the terms of this Agreement, BROAD hereby grants to LICENSEE, solely for academic non-commercial research purposes, a non-exclusive, non-transferable license to: (a) download, execute and display the PROGRAM and (b) create bug fixes and modify the PROGRAM.  LICENSEE hereby automatically grants to BROAD a non-exclusive, royalty-free, irrevocable license to any LICENSEE bug fixes or modifications to the PROGRAM with unlimited rights to sublicense and/or distribute.  LICENSEE agrees to provide any such modifications and bug fixes to BROAD promptly upon their creation.  The LICENSEE may apply the PROGRAM in a pipeline to data owned by users other than the LICENSEE and provide these users the results of the PROGRAM provided LICENSEE does so for academic non-commercial purposes only.  For clarification purposes, academic sponsored research is not a commercial use under the terms of this Agreement.
2.2  No Sublicensing or Additional Rights. LICENSEE shall not sublicense or distribute the PROGRAM, in whole or in part, without prior written permission from BROAD.  LICENSEE shall ensure that all of its users agree to the terms of this Agreement.  LICENSEE further agrees that it shall not put the PROGRAM on a network, server, or other similar technology that may be accessed by anyone other than the LICENSEE and its employees and users who have agreed to the terms of this agreement.
2.3  License Limitations. Nothing in this Agreement shall be construed to confer any rights upon LICENSEE by implication, estoppel, or otherwise to any computer software, trademark, intellectual property, or patent rights of BROAD, or of any other entity, except as expressly granted herein. LICENSEE agrees that the PROGRAM, in whole or part, shall not be used for any commercial purpose, including without limitation, as the basis of a commercial software or hardware product or to provide services. LICENSEE further agrees that the PROGRAM shall not be copied or otherwise adapted in order to circumvent the need for obtaining a license for use of the PROGRAM.

3. OWNERSHIP OF INTELLECTUAL PROPERTY
LICENSEE acknowledges that title to the PROGRAM shall remain with BROAD. The PROGRAM is marked with the following BROAD copyright notice and notice of attribution to contributors. LICENSEE shall retain such notice on all copies.  LICENSEE agrees to include appropriate attribution if any results obtained from use of the PROGRAM are included in any publication.

Copyright 2014 Broad Institute, Inc.
Notice of attribution:  The Oncotator 1.0 program was made available through the generosity of the Broad Institute, Inc.

LICENSEE shall not use any trademark or trade name of BROAD, or any variation, adaptation, or abbreviation, of such marks or trade names, or any names of officers, faculty, students, employees, or agents of BROAD except as states above for attribution purposes.

4. INDEMNIFICATION
LICENSEE shall indemnify, defend, and hold harmless BROAD, and their respective officers, faculty, students, employees, associated investigators and agents, and their respective successors, heirs and assigns, ("Indemnitees"), against any liability, damage, loss, or expense (including reasonable attorney fees and expenses) incurred by or imposed upon any of the Indemnitees in connection with any claims, suits, actions, demands or judgments arising out of any theory of liability (including, without limitation, actions in the form of tort, warranty, or strict liability and regardless of whether such action has any factual basis) pursuant to any right or license granted under this Agreement.

5. NO REPRESENTATIONS OR WARRANTIES
THE PROGRAM IS DELIVERED "AS IS."  BROAD MAKES NO REPRESENTATIONS OR WARRANTIES OF ANY KIND CONCERNING THE PROGRAM OR THE COPYRIGHT, EXPRESS OR IMPLIED, INCLUDING, WITHOUT LIMITATION, WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, NONINFRINGEMENT, OR THE ABSENCE OF LATENT OR OTHER DEFECTS, WHETHER OR NOT DISCOVERABLE. BROAD EXTENDS NO WARRANTIES OF ANY KIND AS TO PROGRAM CONFORMITY WITH WHATEVER USER MANUALS OR OTHER LITERATURE MAY BE ISSUED FROM TIME TO TIME.  IN NO EVENT SHALL BROAD OR ITS RESPECTIVE DIRECTORS, OFFICERS, EMPLOYEES, AFFILIATED INVESTIGATORS AND AFFILIATES BE LIABLE FOR INCIDENTAL OR CONSEQUENTIAL DAMAGES OF ANY KIND, INCLUDING, WITHOUT LIMITATION, ECONOMIC DAMAGES OR INJURY TO PROPERTY AND LOST PROFITS, REGARDLESS OF WHETHER BROAD SHALL BE ADVISED, SHALL HAVE OTHER REASON TO KNOW, OR IN FACT SHALL KNOW OF THE POSSIBILITY OF THE FOREGOING.

6. ASSIGNMENT
This Agreement is personal to LICENSEE and any rights or obligations assigned by LICENSEE without the prior written consent of BROAD shall be null and void.

7. MISCELLANEOUS
7.1 Export Control. LICENSEE gives assurance that it will comply with all United States export control laws and regulations controlling the export of the PROGRAM, including, without limitation, all Export Administration Regulations of the United States Department of Commerce. Among other things, these laws and regulations prohibit, or require a license for, the export of certain types of software to specified countries.
7.2 Termination. LICENSEE shall have the right to terminate this Agreement for any reason upon prior written notice to BROAD. If LICENSEE breaches any provision hereunder, and fails to cure such breach within thirty (30) days, BROAD may terminate this Agreement immediately. Upon termination, LICENSEE shall provide BROAD with written assurance that the original and all copies of the PROGRAM have been destroyed, except that, upon prior written authorization from BROAD, LICENSEE may retain a copy for archive purposes.
7.3 Survival. The following provisions shall survive the expiration or termination of this Agreement: Articles 1, 3, 4, 5 and Sections 2.2, 2.3, 7.3, and 7.4.
7.4 Notice. Any notices under this Agreement shall be in writing, shall specifically refer to this Agreement, and shall be sent by hand, recognized national overnight courier, confirmed facsimile transmission, confirmed electronic mail, or registered or certified mail, postage prepaid, return receipt requested.  All notices under this Agreement shall be deemed effective upon receipt.
7.5 Amendment and Waiver; Entire Agreement. This Agreement may be amended, supplemented, or otherwise modified only by means of a written instrument signed by all parties. Any waiver of any rights or failure to act in a specific instance shall relate only to such instance and shall not be construed as an agreement to waive any rights or fail to act in any other instance, whether or not similar. This Agreement constitutes the entire agreement among the parties with respect to its subject matter and supersedes prior agreements or understandings between the parties relating to its subject matter.
7.6 Binding Effect; Headings. This Agreement shall be binding upon and inure to the benefit of the parties and their respective permitted successors and assigns. All headings are for convenience only and shall not affect the meaning of any provision of this Agreement.
7.7 Governing Law. This Agreement shall be construed, governed, interpreted and applied in accordance with the internal laws of the Commonwealth of Massachusetts, U.S.A., without regard to conflict of laws principles.
"""
import ConfigParser
import logging
import shutil

import unittest
from oncotator.datasources.EnsemblTranscriptDatasource import EnsemblTranscriptDatasource
from oncotator.DatasourceFactory import DatasourceFactory
from oncotator.MutationData import MutationData
from oncotator.datasources.TranscriptProvider import TranscriptProvider
from oncotator.utils.ConfigUtils import ConfigUtils
from oncotator.utils.install.GenomeBuildFactory import GenomeBuildFactory
from test.TestUtils import TestUtils

TestUtils.setupLogging(__file__, __name__)
class EnsemblTranscriptDatasourceTest(unittest.TestCase):
    _multiprocess_can_split_ = True

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_intitialize(self):
        """Test a simple initialization of an ensembl datasource """
        base_config_location = "testdata/ensembl/saccer/"
        config_parser = ConfigUtils.createConfigParser(base_config_location + "ensembl.config")
        title = config_parser.get("general", "title")
        version = config_parser.get("general", "version")
        src_file = config_parser.get("general", "src_file")

        ensembl_ds = EnsemblTranscriptDatasource(title=title, version=version, src_file=src_file)
        self.assertIsNotNone(ensembl_ds)
        ensembl_ds.set_tx_mode(TranscriptProvider.TX_MODE_BEST_EFFECT)
        self.assertTrue(TranscriptProvider.TX_MODE_BEST_EFFECT == ensembl_ds.get_tx_mode())

    def test_overlapping_single_transcripts(self):
        base_config_location = "testdata/ensembl/saccer/"

        ensembl_ds = DatasourceFactory.createDatasource(base_config_location + "ensembl.config", base_config_location)
        recs = ensembl_ds.get_overlapping_transcripts("I", "500", "500")
        self.assertTrue(len(recs) == 1)
        self.assertTrue(recs[0].get_gene() == 'YAL069W')

    def test_overlapping_multiple_transcripts_snp(self):
        base_config_location = "testdata/ensembl/saccer/"

        ensembl_ds = DatasourceFactory.createDatasource(base_config_location + "ensembl.config", base_config_location)
        recs = ensembl_ds.get_overlapping_transcripts("I", "550", "550")
        self.assertTrue(len(recs) == 2)
        ids = set()
        for r in recs:
            ids.add(r.get_transcript_id())

        self.assertTrue(len(ids - set(['YAL069W', 'YAL068W-A'])) == 0)

    def test_overlapping_multiple_transcripts_indel(self):
        base_config_location = "testdata/ensembl/saccer/"

        ensembl_ds = DatasourceFactory.createDatasource(base_config_location + "ensembl.config", base_config_location)
        recs = ensembl_ds.get_overlapping_transcripts("I", "2500", "8000")
        self.assertTrue(len(recs) == 2)
        ids = set()
        for r in recs:
            ids.add(r.get_transcript_id())

        self.assertTrue(len(ids - set(['YAL067W-A', 'YAL067C'])) == 0)

    def _create_ensembl_ds_from_saccer(self):
        gencode_input_gtf = "testdata/Saccharomyces_cerevisiae.EF4.71_trim.gtf"
        gencode_input_fasta = "testdata/Saccharomyces_cerevisiae.EF4.71_trim.cdna.all.fa"
        base_output_filename = "out/test_saccer_ds"
        shutil.rmtree(base_output_filename + ".transcript.idx", ignore_errors=True)
        shutil.rmtree(base_output_filename + ".transcript_by_gene.idx", ignore_errors=True)
        shutil.rmtree(base_output_filename + ".transcript_by_gp_bin.idx", ignore_errors=True)
        genome_build_factory = GenomeBuildFactory()
        genome_build_factory.construct_ensembl_indices([gencode_input_gtf], [gencode_input_fasta], base_output_filename)
        ensembl_ds = EnsemblTranscriptDatasource(base_output_filename, title="ensembl", version="71")
        return ensembl_ds

    def test_simple_annotate_with_nonhuman(self):
        """Test a very simple annotation with a nonhuman genome (saccer)"""
        ensembl_ds = self._create_ensembl_ds_from_saccer()

        m = MutationData()
        m.chr = "I"
        m.start = "500"
        m.end = "500"
        m.ref_allele = "C"
        m.alt_allele = "A"

        m2 = ensembl_ds.annotate_mutation(m)

        self.assertTrue(m2['annotation_transcript'] == "YAL069W")
        self.assertTrue(m2['gene'] == "YAL069W")

    def test_simple_annotate(self):
        """ Annotate a simple example.
        """
        base_config_location = "testdata/ensembl/saccer/"
        config_parser = ConfigUtils.createConfigParser(base_config_location + "ensembl.config")
        title = config_parser.get("general", "title")
        version = config_parser.get("general", "version")
        src_file = config_parser.get("general", "src_file")

        ensembl_ds = EnsemblTranscriptDatasource(title=title, version=version, src_file=src_file)

        m = MutationData()
        m.chr = "22"
        m.start = "22161963"
        m.end = "22161963"
        m.ref_allele = "C"
        m.alt_allele = "A"

        m2 = ensembl_ds.annotate_mutation(m)

    def test_overlapping_multiple_genes(self):
        """Test that we can collect multiple overlapping genes """
        ds = TestUtils._create_test_gencode_ds("out/overlapping_genes_multiple_")
        genes = ds.get_overlapping_genes("22", 22080000, 22120000)
        self.assertTrue(len(set(["MAPK1", "YPEL1"]) - genes) ==0 )

    def test_overlapping_gene(self):
        """Test that we can collect an overlapping gene """
        ds = TestUtils._create_test_gencode_ds("out/overlapping_genes_")
        genes = ds.get_overlapping_genes("22", 22115000, 22120000)
        self.assertTrue(len(set(["MAPK1"]) - genes) == 0)

    def test_overlapping_gene_5flank(self):
        """Test that we can collect an overlapping gene on its 5' Flank """
        ds = TestUtils._create_test_gencode_ds("out/overlapping_genes_flank")
        txs = ds.get_overlapping_transcripts("22", 22222050, 22222050, padding=100)
        self.assertTrue( len(txs) == 1)
        self.assertTrue(txs[0].get_transcript_id() == "ENST00000398822.3")

        txs = ds.get_overlapping_transcripts("22", 22224920, 22224920)
        self.assertTrue(len(txs) == 0)


    def test_small_positive_strand_transcript_change(self):
        """Test one location on a transcript and make sure that the transcript change rendered properly """
        ds = TestUtils._create_test_gencode_ds("out/small_positive_strand_")

        # Now for a negative strand
        m = MutationData()
        m.chr = "22"
        m.start = "22221730"
        m.end = "22221730"
        m.ref_allele = "T"
        m.alt_allele = "G"
        m2 = ds.annotate_mutation(m)
        self.assertTrue(m2['transcript_change'] == "c.1A>C", "Incorrect transcript change: " + m2['transcript_change'])

        # positive strand
        m = MutationData()
        m.chr = "3"
        m.start = "178916614"
        m.end = "178916614"
        m.ref_allele = "G"
        m.alt_allele = "T"
        m2 = ds.annotate_mutation(m)
        self.assertTrue(m2['transcript_change'] == "c.1G>T", "Incorrect transcript change: " + m2['transcript_change'])

    def test_hgvs_annotations_simple_SNP(self):
        """Test that HGVS annotations appear (incl. protein change) in a mutation, so we believe that the Transcript objects are populated properly."""
        ds = TestUtils._create_test_gencode_ds("out/test_hgvs_annotations_")

        # Now for a negative strand
        m = MutationData()
        m.chr = "22"
        m.start = "22221730"
        m.end = "22221730"
        m.ref_allele = "T"
        m.alt_allele = "G"
        m.build = "hg19"
        m2 = ds.annotate_mutation(m)
        self.assertEqual(m2.get('HGVS_genomic_change', None), 'chr22.hg19:g.22221730T>G')
        self.assertEqual(m2.get('HGVS_coding_DNA_change', None), 'ENST00000215832.6:c.1A>C')
        self.assertEqual(m2.get('HGVS_protein_change', None), 'ENSP00000215832:p.Met1Leu')

    def test_hgvs_annotations_IGR(self):
        """Test that the HGVS annotations appear for IGR"""
        ds = TestUtils._create_test_gencode_ds("out/test_hgvs_annotations_IGR_")
        m = MutationData()
        m.createAnnotation('variant_type', 'SNP')
        m.createAnnotation('build', 'hg19')
        m.createAnnotation('variant_classification', 'IGR')
        m.createAnnotation('chr', '15')
        m.createAnnotation('start', 30938316)
        m.createAnnotation('end', 30938316)
        m.createAnnotation('ref_allele', 'G')
        m.createAnnotation('alt_allele', 'A')
        m2 = ds.annotate_mutation(m)
        self.assertEqual(m2.get('HGVS_genomic_change', None), 'chr15.hg19:g.30938316G>A')
        self.assertEqual(m2.get('HGVS_coding_DNA_change', None), '')
        self.assertEqual(m2.get('HGVS_protein_change', None), '')

    def test_no_mapping_file(self):
        """Test that we can still create (from scratch) and instantiate a EnsemblDatasource when no protein mapping is specified (i.e. limited HGVS support)"""
        """Test that HGVS annotations appear (incl. protein change) in a mutation, so we believe that the Transcript objects are populated properly."""
        ds = TestUtils._create_test_gencode_ds("out/test_hgvs_annotations_no_mapping_", protein_id_mapping_file=None)

        # Now for a negative strand
        m = MutationData()
        m.chr = "22"
        m.start = "22221730"
        m.end = "22221730"
        m.ref_allele = "T"
        m.alt_allele = "G"
        m.build = "hg19"
        m2 = ds.annotate_mutation(m)
        self.assertEqual(m2.get('HGVS_genomic_change', None), 'chr22.hg19:g.22221730T>G')
        self.assertEqual(m2.get('HGVS_coding_DNA_change', None), 'ENST00000215832.6:c.1A>C')
        self.assertEqual(m2.get('HGVS_protein_change', None), 'unknown_prot_seq_id:p.Met1Leu')

if __name__ == '__main__':
    unittest.main()
