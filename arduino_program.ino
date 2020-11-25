// motor control program, six stepper motors controlled from a python program.

// ############################################### ################################################# ##########
// Define the ports

// Definition A4998 F
# define  pinEnableF 30                                    // Activate A4998
# define  pinStepF    2                                    // Rising edge = one step.
# define  pinDirF     3                                    // Direction

// Definition A4998 R
# define  pinEnableR  34                                    // Activate A4998
# define  pinStepR    17                                    // Rising edge = one step.
# define  pinDirR     27                                    // Direction

// Definition A4998 B
# define  pinEnableB  38                                    // Activate A4998
# define  pinStepB    10                                    // Rising edge = one step.
# define  pinDirB     22                                    // Direction

// Definition A4998 L
# define  pinEnableL  42                                    // Activate A4998
# define  pinStepL     5                                    // Rising edge = one step.
# define  pinDirL      6                                    // Direction

// Definition A4998 D
# define  pinEnableD   46                                    // Activate A4998
# define  pinStepD     19                                    // Rising edge = one step.
# define  pinDirD      26                                    // Direction

// Definition A4998 U
# define  pinEnableU  50                                    // Activate A4998
# define  pinStepU    16                                    // Rising edge = one step.
# define  pinDirU     20                                    // Direction

# define  pinIRSensor 3                                     // Pin for IR Sensor

// ############################################### ################################################# ##########
// Declaration of the variables

# define  del  320                                          // Delay in microsecond between a rising sling and a falling sling
# define  acc  10                                           // Number of acceleration and deceleration steps to be performed with each movement
# define  vm   800                                          // Slowest speed at start of acceleration
# define  x (vm - del) / acc                                 // variable of acceleration functions

// ############################################### ################################################# ##########
// Table of movements

// All cases F, R, B, L, D, U, #, F ', R', B ', L', D ', U', #, F2, R2, B2, L2, D2, U2 , #, FB, FB ', FB2, F'B, F'B', F'B2, F2B, F2B ', F2B2, #, RL, RL', RL2, R'L, R'L ', R' L2, R2L, R2L ', R2L2, #, DU, DU', DU2, D'U, D'U ', D'U2, D2U, D2U', D2U2
// Order of the array F, R, B, L, D, U,
//                  F ', R', B ', L', D ', U',
//                  F2, R2, B2, L2, D2, U2,
//                  FB, FB ', F'B, F'B',
//                  F2B2, RL, RL ', R'L,
//                  R'L ', R2L2, DU, DU',
//                  D'U, D'U ', D2U2, FB2,
//                  F'B2, F2B, F2B ', RL2,
//                  R'L2, R2L, R2L ', DU2,
//                  D'U2, D2U, D2U '

int Tab [] [ 8 ] = {{ 1 , pinStepF, pinDirF, 0 , 50 }, { 1 , pinStepR, pinDirR, 0 , 50 }, { 1 , pinStepB, pinDirB, 0 , 50 }, { 1 , pinStepL, pinDirL, 0 , 50 }, { 1 , pinStepD, pinDirD, 0 , 50 }, { 1 , pinStepU, pinDirU, 0 , 50 },

               { 1 , pinStepF, pinDirF, 1 , 50 }, { 1 , pinStepR, pinDirR, 1 , 50 }, { 1 , pinStepB, pinDirB, 1 , 50 }, { 1 , pinStepL, pinDirL, 1 , 50 }, { 1 , pinStepD, pinDirD, 1 , 50 }, { 1 , pinStepU, pinDirU, 1 , 50 },
               
               { 1 , pinStepF, pinDirF, 0 , 100 }, { 1 , pinStepR, pinDirR, 0 , 100 }, { 1 , pinStepB, pinDirB, 0 , 100 }, { 1 , pinStepL, pinDirL, 0 , 100 }, { 1 , pinStepD, pinDirD, 0 , 100 }, { 1 , pinStepU, pinDirU, 0 , 100 },
               
               { 2 , pinStepF, pinStepB, pinDirF, pinDirB, 0 , 0 , 50 }, { 2 , pinStepF, pinStepB, pinDirF, pinDirB, 0 , 1 , 50 }, { 2 , pinStepF, pinStepB, pinDirF, pinDirB, 1 , 0 , 50 }, { 2 , pinStepF, pinStepB, pinDirF, pinDirB, 1 , 1 , 50 },

               { 2 , pinStepF, pinStepB, pinDirF, pinDirB, 0 , 0 , 100 }, { 2 , pinStepR, pinStepL, pinDirR, pinDirL, 0 , 0 , 50 }, { 2 , pinStepR, pinStepL, pinDirR, pinDirL, 0 , 1 , 50 }, { 2 , pinStepR, pinStepL, pinDirR, pinDirL, 1 , 0 , 50 },
               
               { 2 , pinStepR, pinStepL, pinDirR, pinDirL, 1 , 1 , 50 }, { 2 , pinStepR, pinStepL, pinDirR, pinDirL, 0 , 0 , 100 }, { 2 , pinStepD, pinStepU, pinDirD, pinDirU, 0 , 0 , 50 }, { 2 , pinStepD, pinStepU, pinDirD, pinDirU, 0 , 1 , 50 },
               
               { 2 , pinStepD, pinStepU, pinDirD, pinDirU, 1 , 0 , 50 }, { 2 , pinStepD, pinStepU, pinDirD, pinDirU, 1 , 1 , 50 }, { 2 , pinStepD, pinStepU, pinDirD, pinDirU, 0 , 0 , 100 }, { 3 , pinStepF, pinStepB, pinDirF, pinDirB, 0 },

               { 3 , pinStepF, pinStepB, pinDirF, pinDirB, 1 }, { 3 , pinStepB, pinStepF, pinDirB, pinDirF, 0 }, { 3 , pinStepB, pinStepF, pinDirB, pinDirF, 1 }, { 3 , pinStepR, pinDirte , pinDirL, 0 },

               { 3 , pinStepR, pinStepL, pinDirR, pinDirL, 1 }, { 3 , pinStepL, pinStepR, pinDirL, pinDirR, 0 }, { 3 , pinStepL, pinStepR, pinDirL, pinDirR, 1 }, { 3 , pinStepD, pinDirtep , pinDirU, 0 },
               
               { 3 , pinStepD, pinStepU, pinDirD, pinDirU, 1 }, { 3 , pinStepU, pinStepD, pinDirU, pinDirD, 0 }, { 3 , pinStepU, pinStepD, pinDirU, pinDirD, 1 }};

// ############################################### ################################################# ##########
// Setup

void  setup () {

Serial. begin ( 9600 );
Serial. println ( " Engine Program " );

// Setup control port (5V)
pinMode (pinEnableF, OUTPUT);
pinMode (pinDirF, OUTPUT);
pinMode (pinStepF, OUTPUT);

// Setup control port (5V)
pinMode (pinEnableR, OUTPUT);
pinMode (pinDirR, OUTPUT);
pinMode (pinStepR, OUTPUT);

// Setup control port (5V)
pinMode (pinEnableB, OUTPUT);
pinMode (pinDirB, OUTPUT);
pinMode (pinStepB, OUTPUT);

// Setup control port (5V)
pinMode (pinEnableL, OUTPUT);
pinMode (pinDirL, OUTPUT);
pinMode (pinStepL, OUTPUT);

// Setup control port (5V)
pinMode (pinEnableD, OUTPUT);
pinMode (pinDirD, OUTPUT);
pinMode (pinStepD, OUTPUT);

// Setup control port (5V)
pinMode (pinEnableU, OUTPUT);
pinMode (pinDirU, OUTPUT);
pinMode (pinStepU, OUTPUT);

// Setup IR sensor
pinMode (pinIRSensor, INPUT)

// Setup of the "pinEnable" ports (blocking of the motor axes)
digitalWrite (pinEnableF, LOW);
digitalWrite (pinEnableR, LOW);
digitalWrite (pinEnableB, LOW);
digitalWrite (pinEnableL, LOW);
digitalWrite (pinEnableD, LOW);
digitalWrite (pinEnableU, LOW);
}
// ############################################### ################################################# ##########
// Movement control method

//
// Only one face turns (regardless of the direction and the direction)
//
void  OneSideMvt ( int pinStep, int pinDir, bool dir, int nbrPas) {
digitalWrite (pinDir, dir);                              // choice of direction
for ( int i = 0 ; i <acc; i ++) {                           // only one face turns
   digitalWrite (pinStep, HIGH);                         // The motor advances by one step (rising edge)
   delayMicroseconds (vm - i * x);
   digitalWrite (pinStep, LOW);                          // falling edge
   delayMicroseconds (vm - i * x);
  }
for ( int i = 0 ; i <nbrPas - 2 * acc; i ++) {                // only one face turns
   digitalWrite (pinStep, HIGH);                         // The motor advances by one step (rising edge)
   delayMicroseconds (del);
   digitalWrite (pinStep, LOW);                          // falling edge
   delayMicroseconds (del);
  }
for ( int i = 0 ; i <acc; i ++) {                           // only one face turns
   digitalWrite (pinStep, HIGH);                         // The motor advances by one step (rising edge)
   delayMicroseconds (del + i * x);
   digitalWrite (pinStep, LOW);                          // falling edge
   delayMicroseconds (del + i * x);
  }
}

//
// Both faces take the same number of steps (regardless of the direction and the direction)
//
void  TwoSidesSameMvt ( int pinStep1, int pinStep2, int pinDir1, int pinDir2, bool dir1, bool dir2, int nbrPas) {
digitalWrite (pinDir1, dir1);
digitalWrite (pinDir2, dir2);
for ( int i = 0 ; i <acc; i ++) {                           // Both faces turn
   digitalWrite (pinStep1, HIGH);                        // Motor1 advances by one step (rising edge)
   digitalWrite (pinStep2, HIGH);                        // Motor2 advances by one step (rising edge)
   delayMicroseconds (vm - i * x);
   digitalWrite (pinStep1, LOW);                         // falling edge
   digitalWrite (pinStep2, LOW);                         // falling edge
   delayMicroseconds (vm - i * x);
  }
for ( int i = 0 ; i <nbrPas - 2 * acc; i ++) {                // Both faces turn
   digitalWrite (pinStep1, HIGH);                        // Motor1 advances by one step (rising edge)
   digitalWrite (pinStep2, HIGH);                        // Motor2 advances by one step (rising edge)
   delayMicroseconds (del);
   digitalWrite (pinStep1, LOW);                         // falling edge
   digitalWrite (pinStep2, LOW);                         // falling edge
   delayMicroseconds (del);
  }
for ( int i = 0 ; i <acc; i ++) {                           // Both faces turn
   digitalWrite (pinStep1, HIGH);                        // Motor1 advances by one step (rising edge)
   digitalWrite (pinStep2, HIGH);                        // Motor2 advances by one step (rising edge)
   delayMicroseconds (del + i * x);
   digitalWrite (pinStep1, LOW);                         // falling edge
   digitalWrite (pinStep2, LOW);                         // falling edge
   delayMicroseconds (del + i * x);
  }
}

//
// one of the two faces is 50 steps, the other is 100 (regardless of the direction and the direction)
//
void  TwoSidesNotSameMvt ( int pinStep1, int pinStep2, int pinDir1, int pinDir2, bool dir1) {
int nbrPas = 50 ;
digitalWrite (pinDir1, dir1);
digitalWrite (pinDir2, dir1);
for ( int i = 0 ; i <acc; i ++) {                           // Both faces turn
   digitalWrite (pinStep1, HIGH);                        // Motor1 advances by one step (rising edge)
   digitalWrite (pinStep2, HIGH);                        // Motor2 advances by one step (rising edge)
   delayMicroseconds (vm - i * x);
   digitalWrite (pinStep1, LOW);                         // falling edge
   digitalWrite (pinStep2, LOW);                         // falling edge
   delayMicroseconds (vm - i * x);
   digitalWrite (pinStep2, HIGH);                        // Motor2 advances by one step (rising edge)
   delayMicroseconds (vm - i * x);
   digitalWrite (pinStep2, LOW);                         // falling edge
   delayMicroseconds (vm - i * x);
  }
for ( int i = 0 ; i <nbrPas - 2 * acc; i ++) {                // Both faces turn
   digitalWrite (pinStep1, HIGH);                        // Motor1 advances by one step (rising edge)
   digitalWrite (pinStep2, HIGH);                        // Motor2 advances by one step (rising edge)
   delayMicroseconds (del);
   digitalWrite (pinStep1, LOW);                         // falling edge
   digitalWrite (pinStep2, LOW);                         // falling edge
   delayMicroseconds (del);
   digitalWrite (pinStep2, HIGH);                        // Motor2 advances by one step (rising edge)
   delayMicroseconds (del);
   digitalWrite (pinStep2, LOW);                         // falling edge
   delayMicroseconds (del);
  }
for ( int i = 0 ; i <acc; i ++) {                           // Both faces turn
   digitalWrite (pinStep1, HIGH);                        // Motor1 advances by one step (rising edge)
   digitalWrite (pinStep2, HIGH);                        // Motor2 advances by one step (rising edge)
   delayMicroseconds (del + i * x);
   digitalWrite (pinStep1, LOW);                         // falling edge
   digitalWrite (pinStep2, LOW);                         // falling edge
   delayMicroseconds (del + i * x);
   digitalWrite (pinStep2, HIGH);                        // Motor2 advances by one step (rising edge)
   delayMicroseconds (del + i * x);
   digitalWrite (pinStep2, LOW);                         // falling edge
   delayMicroseconds (del + i * x);
  }
}

// ############################################### ################################################# ##########

void  loop () {
int statusSensor = digitalRead (pinIRSensor);

if (statusSensor == 1) {
  if (Serial. available ()) {
    int r = Serial. read () - 65 ;                           // r: index of the movement in the Tab array
    if (Tab [r] [ 0 ] == 1 ) {                                  // call the OneSideMvt method
      OneSideMvt (Tab [r] [ 1 ], Tab [r] [ 2 ], Tab [r] [ 3 ], Tab [r] [ 4 ]);
      Serial. print (r);
      }
    else  if (Tab [r] [ 0 ] == 2 ) {                             // call the TwoSidesSameMvt method
      TwoSidesSameMvt (Tab [r] [ 1 ], Tab [r] [ 2 ], Tab [r] [ 3 ], Tab [r] [ 4 ], Tab [r] [ 5 ], Tab [r] [ 6 ], Tab [r] [ 7 ]);
      }
    else  if (Tab [r] [ 0 ] == 3 ) {                             // call the TwoSidesNotSameMvt method
      TwoSidesNotSameMvt (Tab [r] [ 1 ], Tab [r] [ 2 ], Tab [r] [ 3 ], Tab [r] [ 4 ], Tab [r] [ 5 ]);
      }
    }
  }
}
