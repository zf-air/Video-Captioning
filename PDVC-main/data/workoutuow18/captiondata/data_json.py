import csv
import json

def data_json():
    #生成数据集json文件
    #初始的描述，需要把括号里面的与外面的进行替换
    '''
    array = {'action_2': 'Bend your knees until thighs are parallel to the floor.',
             'action_3': 'Raise your hands and place them behind your head.',
             'action_4': 'Without moving your elbows, rotate your forearms up until they are vertical to the floor',
             'action_5': 'Place your hands on your waist.',
             'action_6': 'Raise the left knee in the front of body approximately 45 degrees and place your left foot on the inside of your weight-bearing knee (right knee).',
             'action_7': 'Keeping your foot in contact with this knee, rotate your flexed leg out to the side using your hip muscles and hold for 5 seconds.',
             'action_8': 'Place and press the sole of the left foot on the inner right calf.',
             'action_9': 'Press your palms together in prayer position at your chest, with your thumbs resting on your sternum.',
             'action_10': 'Inhale as you extend your arms overhead, reaching your fingertips to the sky.',
             'action_11': 'Raise the left leg to the front of the body, keeping it straight.',
             'action_12': 'Rotate this leg to the left side and then back to starting position.',
             'action_13': 'Raise the right leg to the front of the body, keeping it straight.',
             'action_14': 'Rotate this leg to the right side and then back to starting position.',
             'action_15': 'Raise the left leg to the front of the body while simultaneously bending forward at the waist, extending the right arm forward, and reaching with the right hand toward the left foot.',
             'action_16': 'Raise the right leg to the front of the body while simultaneously bending forward at the waist, extending the left arm forward, and reaching with the left hand toward the right foot.',
             'action_17': 'Skip in place by hopping on the right leg while bringing the left knee up to waist level.',
             'action_18': 'Switch legs (hopping on the left leg while bringing the right knee up to waist level).',
             'action_19': 'Keeping your hands behind the head, bend your knees until thighs are parallel to the ground.',
             'action_20': 'Step your right foot out to the side while bringing clasped hands in front of your chest.',
             'action_21': 'Bend your left knee until the thigh is parallel to the floor while keeping your right leg is straight.',
             'action_22': 'Engaging your abdominals and pushing your weight into you left heel, slowly stand up on your left leg and raise your right leg.',
             'action_23': 'Bend your right knee until the thigh is parallel to the floor while keeping your left leg is straight.',
             'action_24': 'Press through your right heel to stand, immediately raising you right knee.',
             'action_25': 'Assume holding a barbell across your traps and shoulders, take a large step to the side using the left foot.',
             'action_26': 'Bend your left knee until the thigh is parallel to the floor while keeping your right leg is straight. Push through the left heel to stand and return to the pose in the first step.',
             'action_27': 'Bend your right knee until the thigh is parallel to the floor while keeping your left leg is straight.',
             'action_28': 'Bend your knees until thighs are parallel to the floor while bringing your clasped hands in front of your chest.',
             'action_29': 'Push through your heels to stand up on your right leg, immediately raising you left leg out to the side.',
             'action_30': 'Raise your right arm up in front of your shoulder and your left arm up to the side of your shoulder (your arms should be fully extended at about a 90 degrees angle).',
             'action_31': 'Switch sides to repeat through raising left arm up in the front and right arm up to the side.',
             'action_32': 'Extend arms out to your sides at shoulder height, palms still facing down.',
             'action_33': 'Raise your arms out to shoulder height, bending your elbows 90 degree.',
             'action_34': 'Keeping your knees bend, raise your arms out to shoulder height and bend your elbows 90 degree.',
             'action_35': 'Without moving your elbows and knees, rotate your forearms up until they are vertical to the floor.',
             'action_36': 'Slightly bend your knees, immediately bending your trunk forward (about 45 degrees), and raising your arms to chest height while keeping your palms facing down.',
             'action_37': 'Pull your elbows up straight out to the sides from your shoulders.',
             'action_38': 'Raise your arms out to your shoulder height, keeping arms straight.',
             'action_39': 'Raise your arms up above your head and straighten your elbows until your arms are vertical to the floor.',
             'action_40': 'Bend the trunk to the left, keeping the elbows straight.',
             'action_41': 'Rotate the trunk to the right, keeping the elbows straight.',
             'action_42': 'Skip in place by hopping on the right leg while bringing the left knee up to waist level. Switch legs (hopping on the left leg while bringing the right knee up to waist level).',
             'action_43': 'Step your left foot out to the side while bringing clasped hands in front of your chest.',
             'action_44': 'With your palms facing down, bend both elbows and curl weights in close to your sides. Note: your hands are at your shoulder height.'}
'''

    array = {'action_2': 'Bend your knees until thighs are parallel to the floor.',
             'action_3': 'Raise your hands and place them behind your head.',
             'action_4': 'Without moving your elbows, rotate your forearms up until they are vertical to the floor',
             'action_5': 'Place your hands on your waist.',
             'action_6': 'Raise the left knee in the front of body approximately 45 degrees and place your left foot on the inside of your right knee.',
             'action_7': 'Keeping your foot in contact with this knee, rotate your flexed leg out to the side using your hip muscles and hold for 5 seconds.',
             'action_8': 'Place and press the sole of the left foot on the inner right calf.',
             'action_9': 'Press your palms together in prayer position at your chest, with your thumbs resting on your sternum.',
             'action_10': 'Inhale as you extend your arms overhead, reaching your fingertips to the sky.',
             'action_11': 'Raise the left leg to the front of the body, keeping it straight.',
             'action_12': 'Rotate this leg to the left side and then back to starting position.',
             'action_13': 'Raise the right leg to the front of the body, keeping it straight.',
             'action_14': 'Rotate this leg to the right side and then back to starting position.',
             'action_15': 'Raise the left leg to the front of the body while simultaneously bending forward at the waist, extending the right arm forward, and reaching with the right hand toward the left foot.',
             'action_16': 'Raise the right leg to the front of the body while simultaneously bending forward at the waist, extending the left arm forward, and reaching with the left hand toward the right foot.',
             'action_17': 'Skip in place by hopping on the right leg while bringing the left knee up to waist level.',
             'action_18': 'Hopping on the left leg while bringing the right knee up to waist level.',
             'action_19': 'Keeping your hands behind the head, bend your knees until thighs are parallel to the ground.',
             'action_20': 'Step your right foot out to the side while bringing clasped hands in front of your chest.',
             'action_21': 'Bend your left knee until the thigh is parallel to the floor while keeping your right leg is straight.',
             'action_22': 'Engaging your abdominals and pushing your weight into you left heel, slowly stand up on your left leg and raise your right leg.',
             'action_23': 'Bend your right knee until the thigh is parallel to the floor while keeping your left leg is straight.',
             'action_24': 'Press through your right heel to stand, immediately raising you right knee.',
             'action_25': 'Assume holding a barbell across your traps and shoulders, take a large step to the side using the left foot.',
             'action_26': 'Bend your left knee until the thigh is parallel to the floor while keeping your right leg is straight. Push through the left heel to stand and return to the pose in the first step.',
             'action_27': 'Bend your right knee until the thigh is parallel to the floor while keeping your left leg is straight.',
             'action_28': 'Bend your knees until thighs are parallel to the floor while bringing your clasped hands in front of your chest.',
             'action_29': 'Push through your heels to stand up on your right leg, immediately raising you left leg out to the side.',
             'action_30': 'Raise your right arm up in front of your shoulder and your left arm up to the side of your shoulder.',
             'action_31': 'Switch sides to repeat through raising left arm up in the front and right arm up to the side.',
             'action_32': 'Extend arms out to your sides at shoulder height, palms still facing down.',
             'action_33': 'Raise your arms out to shoulder height, bending your elbows 90 degree.',
             'action_34': 'Keeping your knees bend, raise your arms out to shoulder height and bend your elbows 90 degree.',
             'action_35': 'Without moving your elbows and knees, rotate your forearms up until they are vertical to the floor.',
             'action_36': 'Slightly bend your knees, immediately bending your trunk forward, and raising your arms to chest height while keeping your palms facing down.',
             'action_37': 'Pull your elbows up straight out to the sides from your shoulders.',
             'action_38': 'Raise your arms out to your shoulder height, keeping arms straight.',
             'action_39': 'Raise your arms up above your head and straighten your elbows until your arms are vertical to the floor.',
             'action_40': 'Bend the trunk to the left, keeping the elbows straight.',
             'action_41': 'Rotate the trunk to the right, keeping the elbows straight.',
             'action_42': 'Skip in place by hopping on the right leg while bringing the left knee up to waist level. Hopping on the left leg while bringing the right knee up to waist level.',
             'action_43': 'Step your left foot out to the side while bringing clasped hands in front of your chest.',
             'action_44': 'With your palms facing down, bend both elbows and curl weights in close to your sides.'}
    filename = "WorkoutUOW18.csv"
    Dict = {}  #定义一个字典
    train =['s002','s004','s005','s006','s007','s009','s013','s014']
    valid = ['s003','s008','s011']
    test = ['s001','s010','s012']
    with open(filename) as f:
        reader = csv.reader(f)
        name = 'a001_s001_e001' #设置为文件第一行的名字  test
#        name = 'a001_s002_e001'  # 设置为文件第一行的名字  train
#        name = 'a001_s003_e001'  # 设置为文件第一行的名字  valid
        real_name = 'v_' + name
        duration = 0   #保存子动作的结束时间，直接用最后一个子动作的结束时间作为整个动作的时间总长度
        times = []
        captions = []
       #选择描述的时候，Triceps extension和Prisoner squat 都有action_3
        #但是动作描述不一样，分开讨论,数组里面的是Prisoner squat
        for row in reader:
            if row[0] == 'video-name':
                continue
            m, n, p = row[0].split("_", 2)
            if n in train:
                continue
            if n in valid:
                continue
#            if n in test:
#                continue
            if name == row[0]:
                time = [float(row[1]),float(row[2])]
                if m == 'a017' and row[3] == 'action_3':
                    caption = 'Bend your elbows to lower your hands behind your head.'
                elif row[3] != '':
                    caption = array[row[3]]
                else:
                    caption = ''
                if caption != '':
                    times.append(time)
                    captions.append(caption)
                duration = float(row[2])
                if row[0] == 'a018_s012_e006' and row[3] == 'action_41':
                    Dict[real_name] = {
                        'duration': duration,
                        'timestamps': times,
                        'sentences': captions
                    }
                if row[0] == 'a018_s014_e006' and row[3] == 'action_41':
                    Dict[real_name] = {
                        'duration': duration,
                        'timestamps': times,
                        'sentences': captions
                    }
                if row[0] == 'a018_s011_e006' and row[3] == 'action_41':
                    Dict[real_name] = {
                        'duration': duration,
                        'timestamps': times,
                        'sentences': captions
                    }
            else:
                Dict[real_name] ={
                    'duration':duration,
                    'timestamps':times,
                    'sentences':captions
                }
                name = row[0]
                real_name = 'v_' + name
                duration = float(row[2])
                times = [[float(row[1]), float(row[2])]]
                captions = [array[row[3]]]

    jsObj = json.dumps(Dict, ensure_ascii=False)

    fileObject = open('test.json', 'w')
    fileObject.write(jsObj)
    fileObject.close()


if __name__ == "__main__":
    data_json()