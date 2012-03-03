NAME = iprediaos-i2p-configuration-proxy

VERSION := $(shell awk '/Version:/ { print $$2 }' $(NAME).spec)
RELEASE := $(shell awk '/Release:/ { print $$2 }' $(NAME).spec | sed 's|%{?dist}||g')
TAG=$(NAME)-$(VERSION)-$(RELEASE)

tag:
	@git tag -a -f -m "Tag as $(TAG)" -f $(TAG)
	@echo "Tagged as $(TAG)"

install: 
	@install -D -m 0644 proxy.sh ${DESTDIR}/etc/profile.d/proxy.sh
	@install -D -m 0644 proxy.csh ${DESTDIR}/etc/profile.d/proxy.csh

archive: tag
	@git archive --format=tar --prefix=$(NAME)-$(VERSION)/ HEAD > $(NAME)-$(VERSION).tar
	@bzip2 -f $(NAME)-$(VERSION).tar
	@echo "$(NAME)-$(VERSION).tar.bz2 created"

clean:
	rm -f *~ *bz2
