def getmaze(mazeNo):
    maze_dictionary = {
        "maze1": [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                  [2,0,0,1,0,0,0,0,0,1,0,0,0,0,3],
                  [1,0,0,1,0,0,0,0,0,1,0,0,0,0,1],
                  [1,0,0,1,0,0,1,0,0,1,0,0,1,1,1],
                  [1,0,0,1,0,0,1,0,0,1,0,0,1,1,1],
                  [1,0,0,1,0,0,1,0,0,1,0,0,0,0,1],
                  [1,0,0,1,0,0,1,0,0,1,0,0,0,0,1],
                  [1,0,1,1,0,1,1,1,0,1,1,1,0,0,1],
                  [1,0,0,1,0,0,1,0,0,1,1,1,0,0,1],
                  [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
                  [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1],
                  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                  ],

        "maze2": [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                  [3,0,0,0,0,0,1,1,0,0,0,0,0,0,2],
                  [1,0,0,0,0,0,1,1,0,0,0,0,0,0,1],
                  [1,1,1,1,0,0,1,1,0,0,1,1,1,1,1],
                  [1,0,0,0,0,0,1,1,0,0,0,0,0,0,1],
                  [1,0,0,0,0,0,1,1,0,0,0,0,0,0,1],
                  [1,0,0,1,1,1,1,1,1,1,1,1,0,0,1],
                  [1,0,0,1,1,0,0,0,0,0,1,1,0,0,1],
                  [1,0,0,1,1,0,0,0,0,0,1,1,0,0,1],
                  [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
                  [1,0,0,0,0,0,0,1,0,0,0,0,0,0,1],
                  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                  ],

        "maze3": [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                  [2,0,0,1,0,0,0,0,0,0,0,0,1,1,1],
                  [1,0,0,1,0,0,0,0,0,0,0,0,1,1,1],
                  [1,0,0,1,0,0,1,1,1,1,0,0,1,1,1],
                  [1,0,0,1,0,0,0,0,0,1,0,0,1,1,1],
                  [1,0,0,1,0,0,0,0,0,1,0,0,0,0,1],
                  [1,0,0,1,1,1,1,0,0,1,0,0,0,0,1],
                  [1,0,0,1,0,0,0,0,0,1,1,1,0,0,1],
                  [1,0,0,1,0,0,0,0,0,1,1,1,0,0,1],
                  [1,0,0,0,0,0,1,1,1,1,1,1,0,0,1],
                  [1,0,0,0,0,0,1,1,1,1,1,1,0,0,3],
                  [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                  ],

        "maze4": ['111111111111111',
                  '300000000000001',
                  '100000000000001',
                  '111111111111001',
                  '100000000000001',
                  '100000000000001',
                  '100111111111111',
                  '100100000111002',
                  '100100100111001',
                  '100000100000001',
                  '100000100000001',
                  '111111111111111',
                  ],

        "maze5": ['111111111111111',
                  '300000110000002',
                  '100000110000001',
                  '111100110011111',
                  '111100110011111',
                  '100000110000001',
                  '100000110000001',
                  '100111111111001',
                  '100110000011001',
                  '100000000000001',
                  '100000010000001',
                  '111111111111111',
                  ],

        "trainer1": ['111111111111111',
                     '111111111111111',
                     '111111111111111',
                     '111111111111111',
                     '111111111111111',
                     '200000000000003',
                     '100000000000001',
                     '111111111111111',
                     '111111111111111',
                     '111111111111111',
                     '111111111111111',
                     '111111111111111',
                     ],

        "trainer2": ['111111111111111',
                     '111111111111111',
                     '111111111111111',
                     '111111111111111',
                     '111111111111111',
                     '300000000000002',
                     '100000000000001',
                     '111111111111111',
                     '111111111111111',
                     '111111111111111',
                     '111111111111111',
                     '111111111111111',
                     ],

        "trainer3": ['111111211111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111311111111',
                     ],

        "trainer4": ['111111311111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111211111111',
                     ],

        "trainer5": ['111111111111111',
                     '111111111111111',
                     '111111111111111',
                     '200000001111111',
                     '100000001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111311111111',
                     ],

        "trainer6": ['111111211111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '100000001111111',
                     '300000001111111',
                     '111111111111111',
                     '111111111111111',
                     '111111111111111',
                     ],

        "trainer7": ['111111311111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111000000001',
                     '111111000000002',
                     '111111111111111',
                     '111111111111111',
                     '111111111111111',
                     ],

        "trainer8": ['111111111111111',
                     '111111111111111',
                     '111111111111111',
                     '111111000000003',
                     '111111000000001',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111211111111',
                     ],

        "trainer9": ['111111111111111',
                     '111111111111111',
                     '111111111111111',
                     '111111000000002',
                     '111111000000001',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111001111111',
                     '111111311111111',
                     ],

        "trainer10": ['111111211111111',
                      '111111001111111',
                      '111111001111111',
                      '111111001111111',
                      '111111001111111',
                      '111111001111111',
                      '111111001111111',
                      '111111000000001',
                      '111111000000003',
                      '111111111111111',
                      '111111111111111',
                      '111111111111111',
                      ],

        "trainer11": [[1,1,1,1,1,1,3,1,1,1,1,1,1,1,1],
                      [1,1,1,1,1,1,0,0,1,1,1,1,1,1,1],
                      [1,1,1,1,1,1,0,0,1,1,1,1,1,1,1],
                      [1,1,1,1,1,1,0,0,1,1,1,1,1,1,1],
                      [1,1,1,1,1,1,0,0,1,1,1,1,1,1,1],
                      [1,1,1,1,1,1,0,0,1,1,1,1,1,1,1],
                      [1,1,1,1,1,1,0,0,1,1,1,1,1,1,1],
                      [1,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
                      [2,0,0,0,0,0,0,0,1,1,1,1,1,1,1],
                      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
                      ],

        "trainer12": [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], #14
                      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], #29
                      [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1], #44
                      [3,0,0,0,0,0,0,0,1,1,1,1,1,1,1], #59
                      [1,0,0,0,0,0,0,0,1,1,1,1,1,1,1], #74
                      [1,1,1,1,1,1,0,0,1,1,1,1,1,1,1], #89
                      [1,1,1,1,1,1,0,0,1,1,1,1,1,1,1], #104
                      [1,1,1,1,1,1,0,0,1,1,1,1,1,1,1], #119
                      [1,1,1,1,1,1,0,0,1,1,1,1,1,1,1], #134
                      [1,1,1,1,1,1,0,0,1,1,1,1,1,1,1], #149
                      [1,1,1,1,1,1,0,0,1,1,1,1,1,1,1], #164
                      [1,1,1,1,1,1,2,1,1,1,1,1,1,1,1], #179
                      ],

    }
    return maze_dictionary.get(mazeNo, maze_dictionary["maze1"])
