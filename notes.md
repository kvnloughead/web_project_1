### Feature request

Please note which image files correspond to the images in the brief.  It is tedious to search through them all to find the one you are looking for.

### Typos and Nitpicks

- Duplicate Feynman .png images, one spelled with 'y' and one with 'i'

- Probably shouldn't call it "square-pic" if there isn't a corresponding image file.

- In `texts.md` "Description block" is mislabelled as "Digits block".

### Feedback, etc.

The headers for pages can be pretty inscrutable.  Examples:

    > Block for the whole page, page __page__
    > Add a pair of tags to denote the whole structure of the page

Pardon?

#### Page 06

Why say "Be careful when using min-height"?  Should I be using min-height?

#### Page 1 

#1/  This all is very confusing.  We are told to "assign a place modifer with a header value to the logo block" but the logo block doesn't exist yet.   So we have to create it, I suppose.   But then where?  We are told that footer logo will go in the footer block... but then doesn't that mean that the logo should be named `footer__logo`?  And then we should make the header logo `header__logo`?   But at the same time it seems like we are told use just `logo`, which I think would imply that it should exist outside of the header block.  Or maybe I just don't get BEM.

Related issue... using these settings

```
.logo_place_header {
    position: absolute;
    z-index: 1;
    top: 30px;
    left: 64px;
    width: 154px;
    height: 31px;
    background-image: url('../images/logo.png');
}
```

which I think are correct, leaves the logo partially obscured.   I fixed it by increasing width and height (but then had to also set background to not repeat.)