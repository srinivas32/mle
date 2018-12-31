all: deb

deb:
	{ find . -name '.git*' | xargs rm -rf; } \
		&& rm -f vendor/termbox/waf \
		&& { find .. -maxdepth 1 -type f -name 'mle*' | xargs rm -f; } \
		&& { dh_make -s -y -c apache --createorig || true; } \
		&& debuild -i -us -uc -sa -S \
		&& debsign ../mle*.dsc \
		&& sudo pbuilder --build ../mle*.dsc \
		&& debsign ../mle*.dsc

.PHONY: all deb
