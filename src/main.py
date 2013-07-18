#!/usr/bin/python2

import sys, ConfigParser, subprocess, shutil, os, re
    
import lib.configparser as configparser
import lib.argparser as argparser
import lib.message as message
import lib.misc as misc

import actions.extract as extract
import actions.chroot as chroot
import actions.pkgm as pkgm
import actions.deb as deb
import actions.rebuild as rebuild
import actions.clean as clean

try:
	if not misc.check_uid():
		message.critical('You are not root')
		sys.exit(2)

	if argparser.ARGS.extract:
		message.info('Extracting...')
		extract.main()
    
	if argparser.ARGS.chroot:
		message.info('Chrooting...')
		chroot.main()
	
	if argparser.ARGS.pkgm:
		message.info('Running package manager...')
		pkgm.main()
	
	if argparser.ARGS.deb:
		message.info('Installing Debian package...')
		deb.main()
		
	if argparser.ARGS.rebuild:
		message.info('Rebuilding ISO...')
		rebuild.main()
		
	if argparser.ARGS.clean:
		message.info('Cleaning up...')
		clean.main()
			
except ConfigParser.Error as detail:
	message.critical('CONFIGPARSER' + str(detail))
	sys.exit(3)
except subprocess.CalledProcessError as detail:
	message.critical('SUBPROCESS: ' + str(detail))
	sys.exit(4)
except shutil.Error as detail:
	message.critical('SHUTIL: ' + str(detail))
	sys.exit(7)
except OSError as detail:
	message.critical('OS: ' + str(detail))
	sys.exit(8)
except IOError as detail:
	message.critical('IO: ' + str(detail))
	sys.exit(9)
except re.error as detail:
	message.critical('REGEXP: ' + str(detail))
	sys.exit(10)
except KeyboardInterrupt:
	message.critical('Interupt signal received')
	sys.exit(11)
except SystemExit:
	sys.exit(2)
except:
	message.mark_critical('Unexpected error', sys.exc_info()[0])
	raise
	sys.exit(1)