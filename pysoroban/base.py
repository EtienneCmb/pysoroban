#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import numpy as np


class sorobase(object):

    """Soroban training class."""

    def __init__(self, nb_high=999, nb_size=10, operation='+'):
        """TODO: to be defined1.

        :nb_low: TODO
        :nb_high: TODO
        :nb_type: TODO
        :operation: TODO

        """
        self._nb_low = 1
        self._nb_high = nb_high
        self._operation = operation
        self._nb_size = nb_size

        # Input checking :
        if isinstance(self._operation, str):
            # Turn it into a list :
            self._operation = [k for k in self._operation]
            self._symb = self._operation
            # Check if all operators or possible :
            if not all([k in ['+', '-', '*', '/'] for k in self._operation]):
                raise ValueError("Use symbol '+', '-', '*', '/'")
            # Generate random operation in the list :
            rndop = np.random.randint(0, len(self._operation), self._nb_size)
            self._operation = [self._operation[k] for k in rndop]
            self._operation[0] = '+'

    def run(self, pause=30, inter=True, inf=False):
        # Check inputs :
        if pause is not None:
            if not isinstance(pause, int):
                raise ValueError('pause must be an integer')

        if not inf:
            # Define random numbers :
            nb = np.random.randint(
                self._nb_low, self._nb_high, size=self._nb_size)

            # Transform to string :
            nbstr = [self._operation[num] + str(k) for num, k in enumerate(nb)]

            # Print each operation :
            nbinter = 0
            for num, k in enumerate(nbstr):
                # Print number :
                print(str(num) + ': ' + str(k))
                # Set pause :
                if (pause is not None) and (num is not 0):
                    for i in range(pause):
                        print('Pause: %03ds' % (pause - i), end='\r')
                        time.sleep(1)
                        if i == pause - 1:
                            print('                 ', end='\r')
                elif num is 0:
                    time.sleep(2)
                # Update nbinter :
                nbinter = eval(str(nbinter) + k)
                # Display intermediate result :
                if inter and (num not in [0, len(nb) - 1]):
                    print('          Intermediate: ', nbinter)

            # Print final result :
            print('FINAL RESULT: ', nbinter)
        else:
            var = ''
            q = 0
            nbinter = 0
            while var is '':
                # Define a number :
                nb = np.random.randint(self._nb_low, high=self._nb_high,
                                       size=1)[0]
                # Define random symbole :
                symb = self._symb[np.random.randint(0, len(self._symb), 1)[0]]
                if q == 0:
                    symb = '+'
                print(str(q) + ' :' + symb + str(nb))
                # Define time start :
                start = time.time()
                # Update nbinter :
                nbinter = eval(str(nbinter) + symb + str(nb))
                if q is not 0:
                    # User input :
                    var = input(
                        'Press <enter> to continue or any key to stop: ')
                    endtime = np.round(10 * (time.time() - start))/10
                    print('Result: ' + str(nbinter) +
                          ', Time: ' + str(endtime) + 's\n')
                q += 1
