# Choregraphe bezier export in Python.

names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([1.6, 8.6])
keys.append([[0.06592, [3, -0.533333, 0], [3, 2.33333, 0]], [0.0536479, [3, -2.33333, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([1.6, 8.6])
keys.append([[0.0275701, [3, -0.533333, 0], [3, 2.33333, 0]], [0.00149202, [3, -2.33333, 0], [3, 0, 0]]])

names.append("LAnklePitch")
times.append([1.6, 6.6, 8.6])
keys.append([[-1.18122, [3, -0.533333, 0], [3, 1.66667, 0]], [-1.18276, [3, -1.66667, 0], [3, 0.666667, 0]], [0.0889301, [3, -0.666667, 0], [3, 0, 0]]])

names.append("LAnkleRoll")
times.append([1.6, 6.6, 8.6])
keys.append([[0.075208, [3, -0.533333, 0], [3, 1.66667, 0]], [0.0767419, [3, -1.66667, 0], [3, 0.666667, 0]], [-0.122678, [3, -0.666667, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([1.6, 2.4, 3, 3.8, 4.6, 5.4])
keys.append([[-1.06609, [3, -0.533333, 0], [3, 0.266667, 0]], [-1.28852, [3, -0.266667, 0.0179978], [3, 0.2, -0.0134984]], [-1.30202, [3, -0.2, 0], [3, 0.266667, 0]], [-0.880473, [3, -0.266667, -0.0942478], [3, 0.266667, 0.0942478]], [-0.736529, [3, -0.266667, -0.00638619], [3, 0.266667, 0.00638619]], [-0.730143, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([1.6, 2.4, 3, 3.8, 5.4])
keys.append([[-0.813062, [3, -0.533333, 0], [3, 0.266667, 0]], [-1.69511, [3, -0.266667, 0], [3, 0.2, 0]], [-1.66853, [3, -0.2, -0.0265779], [3, 0.266667, 0.0354373]], [-0.650458, [3, -0.266667, 0], [3, 0.533333, 0]], [-0.785451, [3, -0.533333, 0], [3, 0, 0]]])

names.append("LHand")
times.append([1.6, 2.4, 3, 3.8, 5.4])
keys.append([[0.3964, [3, -0.533333, 0], [3, 0.266667, 0]], [0.9176, [3, -0.266667, -0.0122667], [3, 0.2, 0.00920004]], [0.9268, [3, -0.2, 0], [3, 0.266667, 0]], [0.9168, [3, -0.266667, 0.00493334], [3, 0.533333, -0.00986668]], [0.8824, [3, -0.533333, 0], [3, 0, 0]]])

names.append("LHipPitch")
times.append([1.6, 6.6, 8.6])
keys.append([[-0.722472, [3, -0.533333, 0], [3, 1.66667, 0]], [-0.713267, [3, -1.66667, -0.00920488], [3, 0.666667, 0.00368195]], [0.131966, [3, -0.666667, 0], [3, 0, 0]]])

names.append("LHipRoll")
times.append([1.6, 6.6, 8.6])
keys.append([[-0.075124, [3, -0.533333, 0], [3, 1.66667, 0]], [-0.0735901, [3, -1.66667, -0.00153396], [3, 0.666667, 0.000613586]], [0.0982179, [3, -0.666667, 0], [3, 0, 0]]])

names.append("LHipYawPitch")
times.append([1.6, 6.6, 8.6])
keys.append([[-0.20398, [3, -0.533333, 0], [3, 1.66667, 0]], [-0.202446, [3, -1.66667, -0.00153413], [3, 0.666667, 0.000613652]], [-0.164096, [3, -0.666667, 0], [3, 0, 0]]])

names.append("LKneePitch")
times.append([1.6, 6.6, 8.6])
keys.append([[2.10921, [3, -0.533333, 0], [3, 1.66667, 0]], [2.10768, [3, -1.66667, 0.00153585], [3, 0.666667, -0.000614338]], [-0.0844118, [3, -0.666667, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([1.6, 2.4, 3, 3.8, 4.6, 5.4])
keys.append([[1.4005, [3, -0.533333, 0], [3, 0.266667, 0]], [-0.196393, [3, -0.266667, 0.0429933], [3, 0.2, -0.032245]], [-0.228638, [3, -0.2, 0], [3, 0.266667, 0]], [-0.185656, [3, -0.266667, -0.0429822], [3, 0.266667, 0.0429822]], [0.593412, [3, -0.266667, 0], [3, 0.266667, 0]], [0.380482, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([1.6, 2.4, 3, 3.8, 4.6, 5.4])
keys.append([[0.147222, [3, -0.533333, 0], [3, 0.266667, 0]], [1.09063, [3, -0.266667, -0.00724655], [3, 0.2, 0.00543491]], [1.09607, [3, -0.2, 0], [3, 0.266667, 0]], [0.538392, [3, -0.266667, 0.15068], [3, 0.266667, -0.15068]], [0.191986, [3, -0.266667, 0.0961316], [3, 0.266667, -0.0961316]], [-0.0383972, [3, -0.266667, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([1.6, 2.4, 3, 3.8, 5.4])
keys.append([[0.13495, [3, -0.533333, 0], [3, 0.266667, 0]], [-1.45121, [3, -0.266667, 0.028635], [3, 0.2, -0.0214763]], [-1.47268, [3, -0.2, 0], [3, 0.266667, 0]], [-1.45888, [3, -0.266667, -0.00835179], [3, 0.533333, 0.0167036]], [-1.39752, [3, -0.533333, 0], [3, 0, 0]]])

names.append("RAnklePitch")
times.append([1.6, 6.6, 8.6])
keys.append([[-1.18574, [3, -0.533333, 0], [3, 1.66667, 0]], [-1.1796, [3, -1.66667, -0.00613646], [3, 0.666667, 0.00245458]], [0.0859461, [3, -0.666667, 0], [3, 0, 0]]])

names.append("RAnkleRoll")
times.append([1.6, 6.6, 8.6])
keys.append([[-0.0758698, [3, -0.533333, 0], [3, 1.66667, 0]], [-0.076658, [3, -1.66667, 0], [3, 0.666667, 0]], [0.12583, [3, -0.666667, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([1.6, 2.4, 3, 3.8, 4.6, 5.4])
keys.append([[1.05697, [3, -0.533333, 0], [3, 0.266667, 0]], [1.284, [3, -0.266667, -0.0240203], [3, 0.2, 0.0180152]], [1.30202, [3, -0.2, 0], [3, 0.266667, 0]], [0.889762, [3, -0.266667, 0.0942478], [3, 0.266667, -0.0942478]], [0.736529, [3, -0.266667, 0.00476826], [3, 0.266667, -0.00476826]], [0.731761, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([1.6, 2.4, 3, 3.8, 5.4])
keys.append([[0.806841, [3, -0.533333, 0], [3, 0.266667, 0]], [1.69656, [3, -0.266667, 0], [3, 0.2, 0]], [1.66853, [3, -0.2, 0.0280266], [3, 0.266667, -0.0373688]], [0.647306, [3, -0.266667, 0], [3, 0.533333, 0]], [0.750085, [3, -0.533333, 0], [3, 0, 0]]])

names.append("RHand")
times.append([1.6, 2.4, 3, 3.8, 5.4])
keys.append([[0, [3, -0.533333, 0], [3, 0.266667, 0]], [0, [3, -0.266667, 0], [3, 0.2, 0]], [0, [3, -0.2, 0], [3, 0.266667, 0]], [0, [3, -0.266667, 0], [3, 0.533333, 0]], [0, [3, -0.533333, 0], [3, 0, 0]]])

names.append("RHipPitch")
times.append([1.6, 6.6, 8.6])
keys.append([[-0.717953, [3, -0.533333, 0], [3, 1.66667, 0]], [-0.717953, [3, -1.66667, 0], [3, 0.666667, 0]], [0.128814, [3, -0.666667, 0], [3, 0, 0]]])

names.append("RHipRoll")
times.append([1.6, 6.6, 8.6])
keys.append([[0.073674, [3, -0.533333, 0], [3, 1.66667, 0]], [0.07214, [3, -1.66667, 0.00153397], [3, 0.666667, -0.000613589]], [-0.0981341, [3, -0.666667, 0], [3, 0, 0]]])

names.append("RHipYawPitch")
times.append([1.6, 6.6, 8.6])
keys.append([[-0.20398, [3, -0.533333, 0], [3, 1.66667, 0]], [-0.202446, [3, -1.66667, -0.00153413], [3, 0.666667, 0.000613652]], [-0.164096, [3, -0.666667, 0], [3, 0, 0]]])

names.append("RKneePitch")
times.append([1.6, 6.6, 8.6])
keys.append([[2.11082, [3, -0.533333, 0], [3, 1.66667, 0]], [2.11255, [3, -1.66667, 0], [3, 0.666667, 0]], [-0.0923279, [3, -0.666667, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([1.6, 2.4, 3, 3.8, 4.6, 5.4])
keys.append([[1.43587, [3, -0.533333, 0], [3, 0.266667, 0]], [-0.179436, [3, -0.266667, 0.0656034], [3, 0.2, -0.0492026]], [-0.228638, [3, -0.2, 0], [3, 0.266667, 0]], [-0.190175, [3, -0.266667, -0.0384636], [3, 0.266667, 0.0384636]], [0.593412, [3, -0.266667, 0], [3, 0.266667, 0]], [0.380482, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([1.6, 2.4, 3, 3.8, 4.6, 5.4])
keys.append([[-0.165714, [3, -0.533333, 0], [3, 0.266667, 0]], [-1.09225, [3, -0.266667, 0.00508939], [3, 0.2, -0.00381704]], [-1.09607, [3, -0.2, 0], [3, 0.266667, 0]], [-0.541544, [3, -0.266667, -0.15068], [3, 0.266667, 0.15068]], [-0.191986, [3, -0.266667, -0.0966569], [3, 0.266667, 0.0966569]], [0.0383972, [3, -0.266667, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([1.6, 2.4, 3, 3.8, 5.4])
keys.append([[0, [3, -0.533333, 0], [3, 0.266667, 0]], [0, [3, -0.266667, 0], [3, 0.2, 0]], [0, [3, -0.2, 0], [3, 0.266667, 0]], [0, [3, -0.266667, 0], [3, 0.533333, 0]], [0, [3, -0.533333, 0], [3, 0, 0]]])

