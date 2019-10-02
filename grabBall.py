# Choregraphe bezier export in Python.
names = list()
times = list()
keys = list()

names.append("HeadPitch")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 16.5])
keys.append([[0.0674542, [3, -0.833333, 0], [3, 0.833333, 0]], [0.0674542, [3, -0.833333, 0], [3, 0.833333, 0]], [0.0674542, [3, -0.833333, 0], [3, 0.833333, 0]], [0.0674542, [3, -0.833333, 0], [3, 0.833333, 0]], [0.0674542, [3, -0.833333, 0], [3, 0.5, 0]], [0.0735901, [3, -0.5, 0], [3, 0.833333, 0]], [0.0674542, [3, -0.833333, 0], [3, 0, 0]]])

names.append("HeadYaw")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 16.5])
keys.append([[-0.0261199, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.0261199, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.0261199, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.0261199, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.0261199, [3, -0.833333, 0], [3, 0.5, 0]], [-0.0107799, [3, -0.5, 0], [3, 0.833333, 0]], [-0.0261199, [3, -0.833333, 0], [3, 0, 0]]])

names.append("LAnklePitch")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 16.5])
keys.append([[-1.18736, [3, -0.833333, 0], [3, 0.833333, 0]], [-1.18736, [3, -0.833333, 0], [3, 0.833333, 0]], [-1.18736, [3, -0.833333, 0], [3, 0.833333, 0]], [-1.18736, [3, -0.833333, 0], [3, 0.833333, 0]], [-1.18736, [3, -0.833333, 0], [3, 0.5, 0]], [-1.18889, [3, -0.5, 0], [3, 0.833333, 0]], [-0.136568, [3, -0.833333, 0], [3, 0, 0]]])

names.append("LAnkleRoll")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 16.5])
keys.append([[0.0690719, [3, -0.833333, 0], [3, 0.833333, 0]], [0.0690719, [3, -0.833333, 0], [3, 0.833333, 0]], [0.0690719, [3, -0.833333, 0], [3, 0.833333, 0]], [0.0690719, [3, -0.833333, 0], [3, 0.833333, 0]], [0.0690719, [3, -0.833333, 0], [3, 0.5, 0]], [0.06447, [3, -0.5, 0.00460191], [3, 0.833333, -0.00766985]], [-0.0536479, [3, -0.833333, 0], [3, 0, 0]]])

names.append("LElbowRoll")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 15.5])
keys.append([[-0.961776, [3, -0.833333, 0], [3, 0.833333, 0]], [-1.53719, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.34971, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.477032, [3, -0.833333, 0.0294018], [3, 0.833333, -0.0294018]], [-0.526121, [3, -0.833333, 0.0490891], [3, 0.5, -0.0294535]], [-1.35295, [3, -0.5, 0], [3, 0.5, 0]], [-0.862065, [3, -0.5, 0], [3, 0, 0]]])

names.append("LElbowYaw")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 15.5])
keys.append([[-0.851412, [3, -0.833333, 0], [3, 0.833333, 0]], [-1.66307, [3, -0.833333, 0], [3, 0.833333, 0]], [-1.46348, [3, -0.833333, -0.199589], [3, 0.833333, 0.199589]], [-0.303775, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.47865, [3, -0.833333, 0], [3, 0.5, 0]], [-0.477115, [3, -0.5, 0], [3, 0.5, 0]], [-0.515466, [3, -0.5, 0], [3, 0, 0]]])

names.append("LHand")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 15.5])
keys.append([[0.0224, [3, -0.833333, 0], [3, 0.833333, 0]], [0.8396, [3, -0.833333, 0], [3, 0.833333, 0]], [0.8396, [3, -0.833333, 0], [3, 0.833333, 0]], [0.8396, [3, -0.833333, 0], [3, 0.833333, 0]], [0.8396, [3, -0.833333, 0], [3, 0.5, 0]], [0.8364, [3, -0.5, 0], [3, 0.5, 0]], [0.8372, [3, -0.5, 0], [3, 0, 0]]])

names.append("LHipPitch")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 16.5])
keys.append([[-0.699462, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.699462, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.699462, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.699462, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.699462, [3, -0.833333, 0], [3, 0.5, 0]], [-0.705598, [3, -0.5, 0], [3, 0.833333, 0]], [-0.159494, [3, -0.833333, 0], [3, 0, 0]]])

names.append("LHipRoll")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 16.5])
keys.append([[-0.0843279, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.0843279, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.0843279, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.0843279, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.0843279, [3, -0.833333, 0], [3, 0.5, 0]], [-0.0797259, [3, -0.5, -0.00460192], [3, 0.833333, 0.00766986]], [0.066004, [3, -0.833333, 0], [3, 0, 0]]])

names.append("LHipYawPitch")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 16.5])
keys.append([[-0.248467, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.248467, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.248467, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.248467, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.248467, [3, -0.833333, 0], [3, 0.5, 0]], [-0.256136, [3, -0.5, 0], [3, 0.833333, 0]], [-0.156426, [3, -0.833333, 0], [3, 0, 0]]])

names.append("LKneePitch")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 16.5])
keys.append([[2.11075, [3, -0.833333, 0], [3, 0.833333, 0]], [2.11075, [3, -0.833333, 0], [3, 0.833333, 0]], [2.11075, [3, -0.833333, 0], [3, 0.833333, 0]], [2.11075, [3, -0.833333, 0], [3, 0.833333, 0]], [2.11075, [3, -0.833333, 0], [3, 0.5, 0]], [2.11228, [3, -0.5, 0], [3, 0.833333, 0]], [0.460158, [3, -0.833333, 0], [3, 0, 0]]])

names.append("LShoulderPitch")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 15.5])
keys.append([[1.50481, [3, -0.833333, 0], [3, 0.833333, 0]], [1.13792, [3, -0.833333, 0.121711], [3, 0.833333, -0.121711]], [0.774544, [3, -0.833333, 0.0958311], [3, 0.833333, -0.0958311]], [0.562937, [3, -0.833333, 0.169237], [3, 0.833333, -0.169237]], [-0.24088, [3, -0.833333, 0], [3, 0.5, 0]], [0.193243, [3, -0.5, -0.194818], [3, 0.5, 0.194818]], [0.928028, [3, -0.5, 0], [3, 0, 0]]])

names.append("LShoulderRoll")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 15.5])
keys.append([[0.251533, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.216335, [3, -0.833333, 0.0889734], [3, 0.833333, -0.0889734]], [-0.305309, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.247016, [3, -0.833333, -0.0263338], [3, 0.833333, 0.0263338]], [-0.147306, [3, -0.833333, -0.0712672], [3, 0.5, 0.0427603]], [0.095066, [3, -0.5, 0], [3, 0.5, 0]], [-0.153442, [3, -0.5, 0], [3, 0, 0]]])

names.append("LWristYaw")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 15.5])
keys.append([[0.138018, [3, -0.833333, 0], [3, 0.833333, 0]], [0.222388, [3, -0.833333, 0], [3, 0.833333, 0]], [0.161028, [3, -0.833333, 0.06136], [3, 0.833333, -0.06136]], [-1.18276, [3, -0.833333, 0], [3, 0.833333, 0]], [-1.07691, [3, -0.833333, 0], [3, 0.5, 0]], [-1.17355, [3, -0.5, 0], [3, 0.5, 0]], [-1.12753, [3, -0.5, 0], [3, 0, 0]]])

names.append("RAnklePitch")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 16.5])
keys.append([[-1.18267, [3, -0.833333, 0], [3, 0.833333, 0]], [-1.18267, [3, -0.833333, 0], [3, 0.833333, 0]], [-1.18267, [3, -0.833333, 0], [3, 0.833333, 0]], [-1.18267, [3, -0.833333, 0], [3, 0.833333, 0]], [-1.18267, [3, -0.833333, 0], [3, 0.5, 0]], [-1.18114, [3, -0.5, -0.00153411], [3, 0.833333, 0.00255686]], [-0.145688, [3, -0.833333, 0], [3, 0, 0]]])

names.append("RAnkleRoll")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 16.5])
keys.append([[-0.0758698, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.0758698, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.0758698, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.0758698, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.0758698, [3, -0.833333, 0], [3, 0.5, 0]], [-0.0720561, [3, -0.5, -0.00381372], [3, 0.833333, 0.0063562]], [0.0337899, [3, -0.833333, 0], [3, 0, 0]]])

names.append("RElbowRoll")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 15.5])
keys.append([[0.948054, [3, -0.833333, 0], [3, 0.833333, 0]], [1.53949, [3, -0.833333, 0], [3, 0.833333, 0]], [0.497058, [3, -0.833333, 0], [3, 0.833333, 0]], [0.605971, [3, -0.833333, 0], [3, 0.833333, 0]], [0.592166, [3, -0.833333, 0], [3, 0.5, 0]], [1.442, [3, -0.5, 0], [3, 0.5, 0]], [1.11526, [3, -0.5, 0], [3, 0, 0]]])

names.append("RElbowYaw")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 15.5])
keys.append([[0.826783, [3, -0.833333, 0], [3, 0.833333, 0]], [1.3238, [3, -0.833333, -0.0291452], [3, 0.833333, 0.0291452]], [1.35295, [3, -0.833333, 0], [3, 0.833333, 0]], [0.414139, [3, -0.833333, 0], [3, 0.833333, 0]], [0.470897, [3, -0.833333, -0.0567581], [3, 0.5, 0.0340549]], [0.694859, [3, -0.5, 0], [3, 0.5, 0]], [0.547595, [3, -0.5, 0], [3, 0, 0]]])

names.append("RHand")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 15.5])
keys.append([[0.0136, [3, -0.833333, 0], [3, 0.833333, 0]], [0.948, [3, -0.833333, 0], [3, 0.833333, 0]], [0.948, [3, -0.833333, 0], [3, 0.833333, 0]], [0.948, [3, -0.833333, 0], [3, 0.833333, 0]], [0.948, [3, -0.833333, 0], [3, 0.5, 0]], [0.9372, [3, -0.5, 0], [3, 0.5, 0]], [0.946, [3, -0.5, 0], [3, 0, 0]]])

names.append("RHipPitch")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 16.5])
keys.append([[-0.70108, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.705682, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.705682, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.705682, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.705682, [3, -0.833333, 0], [3, 0.5, 0]], [-0.705682, [3, -0.5, 0], [3, 0.833333, 0]], [-0.144238, [3, -0.833333, 0], [3, 0, 0]]])

names.append("RHipRoll")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 16.5])
keys.append([[0.0798099, [3, -0.833333, 0], [3, 0.833333, 0]], [0.0798099, [3, -0.833333, 0], [3, 0.833333, 0]], [0.0798099, [3, -0.833333, 0], [3, 0.833333, 0]], [0.0798099, [3, -0.833333, 0], [3, 0.833333, 0]], [0.0798099, [3, -0.833333, 0], [3, 0.5, 0]], [0.0828778, [3, -0.5, 0], [3, 0.833333, 0]], [-0.0720561, [3, -0.833333, 0], [3, 0, 0]]])

names.append("RHipYawPitch")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 16.5])
keys.append([[-0.248467, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.248467, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.248467, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.248467, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.248467, [3, -0.833333, 0], [3, 0.5, 0]], [-0.256136, [3, -0.5, 0], [3, 0.833333, 0]], [-0.156426, [3, -0.833333, 0], [3, 0, 0]]])

names.append("RKneePitch")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 16.5])
keys.append([[2.10316, [3, -0.833333, 0], [3, 0.833333, 0]], [2.10316, [3, -0.833333, 0], [3, 0.833333, 0]], [2.10316, [3, -0.833333, 0], [3, 0.833333, 0]], [2.10316, [3, -0.833333, 0], [3, 0.833333, 0]], [2.10316, [3, -0.833333, 0], [3, 0.5, 0]], [2.11235, [3, -0.5, 0], [3, 0.833333, 0]], [0.418823, [3, -0.833333, 0], [3, 0, 0]]])

names.append("RShoulderPitch")
times.append([2.5, 5.5, 7.5, 10, 12.5, 14, 15.5])
keys.append([[1.50796, [3, -0.833333, 0], [3, 1, 0]], [1.06414, [3, -1, 0.131857], [3, 0.666667, -0.0879049]], [0.848677, [3, -0.666667, 0.0681044], [3, 0.833333, -0.0851305]], [0.604439, [3, -0.833333, 0.169563], [3, 0.833333, -0.169563]], [-0.168698, [3, -0.833333, 0], [3, 0.5, 0]], [0.357464, [3, -0.5, -0.194562], [3, 0.5, 0.194562]], [0.998676, [3, -0.5, 0], [3, 0, 0]]])

names.append("RShoulderRoll")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 15.5])
keys.append([[-0.270025, [3, -0.833333, 0], [3, 0.833333, 0]], [-0.203136, [3, -0.833333, -0.0668887], [3, 0.833333, 0.0668887]], [0.297067, [3, -0.833333, 0], [3, 0.833333, 0]], [0.16563, [3, -0.833333, 0], [3, 0.833333, 0]], [0.182504, [3, -0.833333, 0], [3, 0.5, 0]], [-0.0782759, [3, -0.5, 0.0547126], [3, 0.5, -0.0547126]], [-0.145772, [3, -0.5, 0], [3, 0, 0]]])

names.append("RWristYaw")
times.append([2.5, 5, 7.5, 10, 12.5, 14, 15.5])
keys.append([[-0.093616, [3, -0.833333, 0], [3, 0.833333, 0]], [0.076658, [3, -0.833333, 0], [3, 0.833333, 0]], [0.06592, [3, -0.833333, 0], [3, 0.833333, 0]], [1.15046, [3, -0.833333, 0], [3, 0.833333, 0]], [1.08296, [3, -0.833333, 0.0674954], [3, 0.5, -0.0404972]], [0.803775, [3, -0.5, 0], [3, 0.5, 0]], [0.931096, [3, -0.5, 0], [3, 0, 0]]])

