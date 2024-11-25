def AudioMenu():
    print("Audio")
    AudioMenuInput = input("Choose ()")

def LightingMenu():
    def ColorsMenu():
        print("Colors")
        print("1. RGB")
        print("2. CMY")
        ColorsMenuInput = input("Choose input color code ()")

    def PositionMenu():
        def EightBitCalc():
            print("degrees to 8-bit Calculator")
            MaxAngle = int(input("Max fixture angle ="))
            MinAngle = int(input("Min fixture angle ="))
            WantedAngle = int(input("What angle do you want the fixture to be at?:"))
            Totalangle = abs(MaxAngle) + abs(MinAngle)
            OneBit = Totalangle / 255
            CalculatedAngle = OneBit * WantedAngle
            if CalculatedAngle < 0:
                CalculatedAngle = CalculatedAngle + 255
                print(f"The 8-bit value of the wanted angle = {CalculatedAngle}")
            else:
                print(f"The 8-bit Value of the wanted angle = {CalculatedAngle}")

        def DegreeCalc():
            print("8-bit to degrees Calculator")
            MaxAngle = int(input("Max fixture angle ="))
            MinAngle = int(input("Min fixture angle ="))
            BitValue = int(input("What is the 8-bit value?:"))
            if BitValue > 255:
                print("Please input an 8-bit value (0-255)")
                DegreeCalc()
            elif BitValue < 0:
                print("Please input an 8-bit value (0-255)")

            TotalAngle = abs(MinAngle) + abs(MaxAngle)
            Center = TotalAngle / 2
            OneBit = TotalAngle / 255
            WantedBitValue = OneBit * BitValue
            CorrectedBitValue = WantedBitValue - Center
            print(f"The calculated angle = {CorrectedBitValue}")

        print("Position")
        print("1. 8-bit (0-255)")
        print("2. degrees")
        PositionMenuInput = input("Choose output position value")
        if PositionMenuInput == "1":
            EightBitCalc()
        elif PositionMenuInput == "2":
            DegreeCalc()
        else:
            print("Input invalid, choose a number between 1-2")
            PositionMenu()

    print("Lighting")
    print("1. Colors")
    print("2. Position")
    LightingMenuInput = input("Choose ()")
    if LightingMenuInput == "1":
        ColorsMenu()
    elif LightingMenuInput == "2":
        PositionMenu()
    else:
        print("Input invalid, Choose a number between 1-2")
        LightingMenu()

def MainMenu ():
    print("Welcome to The Technicians Toolbox")
    print("1. Audio")
    print("2. Lighting")
    MainMenuInput = input("Choose (1-2)")
    if MainMenuInput == "1":
        AudioMenu()
    elif MainMenuInput == "2":
        LightingMenu()
    else:
        print("Input Invalid, Choose a number between 1-2")
        MainMenu()