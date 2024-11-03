class Candidate:
    def __init__(self, name=None, hmdb_identification=None, detection_status=None, smiles_id=None, clas=None,
                 formula=None):
        self.COMMON_NAME = name
        self.HMDB_ID = hmdb_identification
        self.STATUS = detection_status
        self.SMILES = smiles_id
        self.CLASS = clas
        self.CHEMICAL_FORMULA = formula


def results(initial_candidates):
    statuses = [
    'detected and quantified',
    'detected but not quantified',
    'expected but not quantified',
    'predicted'
]
    final_compounds = []
    for status in statuses:
        final_compounds.extend([cand for cand in initial_candidates if cand.STATUS.lower() == status])
        if final_compounds:
            break

    if final_compounds and final_compounds[0].STATUS != 'detected and quantified':
        print(f'\nThe following compound(s) are {final_compounds[0].STATUS.lower()}')
    for i, current_candidate in enumerate(final_compounds):
        print(f'\n'
              f'Compound {i + 1}:\n'
              f'Name: {current_candidate.COMMON_NAME}\n'
              f'Class: {current_candidate.CLASS}\n'
              f'HMDB ID: {current_candidate.HMDB_ID}\n'
              f'SMILES: {current_candidate.SMILES}\n'
              f'Chemical formula: {current_candidate.CHEMICAL_FORMULA}\n')
