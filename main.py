import csv
import glob
import os

candidate_folder = 'D:\\sort\\candidates\\'


def init_ranks():
    """load ranks from csv file"""
    candidates = {}

    with open(candidate_folder + 'candidats.csv') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        for row in reader:
            candidates[row[0]] = {'rank': int(row[1])}

    return candidates


def init_positions():
    """load positions from csv file"""

    available_positions = {}

    with open(candidate_folder + 'postes_disponibles.csv') as f:
        reader = csv.reader(f, delimiter=';')
        next(reader)
        for row in reader:
            available_positions[row[0]] = int(row[1])

    return available_positions


def add_choice_to_candidate_object(candidate_choice, new_rank, choice):
    """add candidate choice to candidate list"""
    
    if candidate_choice.get(new_rank):
        candidate_choice[new_rank].append(choice)
    else:
        candidate_choice[new_rank] = [choice]
    return candidate_choice


def init_choices(candidates):
    """init candidate choices from their csv file"""
    
    for file_path in glob.glob(candidate_folder + '*.csv'):
        if 'candidats.csv' in file_path or 'postes_disponibles.csv' in file_path:
            continue

        with open(file_path, 'r') as f:
            reader = csv.reader(f, delimiter=';')
            candidate_choice = {}

            matricule = os.path.splitext(os.path.basename(file_path))[0]

            for row in reader:
                for index in range(8):
                    if row[3 * index]:
                        candidate_choice = add_choice_to_candidate_object(candidate_choice, int(row[3 * index]), row[3 * index + 1])

            candidates[matricule]['choice'] = candidate_choice
    return candidates


def validate_choices(candidates):
    """check and print errors"""

    is_error = False
    for matricule in candidates.keys():
        rank: int = candidates[matricule]['rank']
        choice = candidates[matricule]['choice']
        erreurs = []
        rank_index: int
        for rank_index in range(1, rank + 1):
            if not choice.get(rank_index):
                erreurs.append('choix ' + str(rank_index) + ' non formulé.')
                continue
            elif len(choice[rank_index]) > 1:
                erreurs.append('plusieurs choix formulés en position ' + str(rank_index) + ' : ' + str(choice[rank_index]))
                continue
            choice[rank_index] = choice[rank_index][0]
        if len(erreurs):
            is_error = True
            print()
            print('le candidat ' + matricule + ' a des erreurs dans sa liste de choix : ')
            for erreur in erreurs:
                print('   - ' + erreur)
        else:
            candidates[matricule]['choice'] = choice
    if is_error:
        candidates = None
    return candidates


def make_choices(available_positions, candidates):
    """make choices"""

    for matricule in candidates.keys():
        rank = candidates[matricule]['rank']
        choice = candidates[matricule]['choice']
        for rank_index in range(1, rank + 1):
            if available_positions.get(choice[rank_index]):
                available_positions[choice[rank_index]] = available_positions[choice[rank_index]] - 1
                candidates[matricule]['attribution'] = choice[rank_index]
                break
    return candidates


def main():
    """main program"""

    candidates = init_ranks()
    # print(candidates)
    candidates = init_choices(candidates)
    # print(candidates)
    candidates = validate_choices(candidates)
    if candidates:
        # print(candidates)
        available_positions = init_positions()
        # print(available_positions)
        candidates = make_choices(available_positions, candidates)
        # print(candidates)
        # print()
        for matricule in candidates:
            print('choix définitif de ' + matricule + ' : ' + candidates[matricule]['attribution'])


main()
