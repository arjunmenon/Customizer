VERSION = 4.0.0
DESTDIR =
BINDIR = /usr/sbin
ETCDIR = /etc
SHAREDIR = /usr/share

all: static

static: clean
	mkdir -p build
	cd build && python2 ../pyinstaller/pyinstaller.py --strip --onefile --name=customizer --noconfirm ../src/main.py
	
install:
	install -vdm755 $(DESTDIR)/$(ETCDIR)/spm $(DESTDIR)/$(BINDIR) $(DESTDIR)/$(SHAREDIR)/customizer/
	install -vm755 build/dist/customizer $(DESTDIR)/$(BINDIR)/customizer
	install -vm644 data/customizer.conf $(DESTDIR)/$(ETCDIR)/
	install -vm644 data/exclude.list $(DESTDIR)/$(SHAREDIR)/customizer/

uninstall:
	$(RM) $(DESTDIR)/$(BINDIR)/customizer
	$(RM) $(DESTDIR)/$(ETCDIR)/customizer.conf
	$(RM) $(DESTDIR)/$(SHAREDIR)/customizer/

bump:
	sed 's|^app_version.*|app_version = "$(VERSION)"|' -i src/lib/argparser.py
	git log > ChangeLog

dist: clean
	git archive HEAD --prefix=customizer-$(VERSION)/ | xz > customizer-$(VERSION).tar.xz

clean:
	$(RM) -r build $(shell find -name '*.pyc') *.tar.xz

.PHONY: all bump static install uninstall dist clean