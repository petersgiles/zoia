The creation of this patch got me back into making patches. And the impetus for that was the arrival of the SSBS Pretty Years, a rare distortion/filter unit that uses sub mini tubes and some wild routing. I will be posting a proper comparison following a patch explorer video; the two are surprisingly close despite using digital dirt on the ZOIA.
_________________________________

Basic idea: overdrive/distortion/fuzz pedal on the surface with 4 gain stages and passive EQ. Underneath is this complex routing that comes about when you introduce the voltage-controlled filter section. There are 4 insert points for the VCF (between each gain stage). Here’s a quick guide on what a single activated insert looks like at each separate stage:

INPUT – PREGAIN – VCF – T1 – T2 – T3 – EQ – OUTPUT (1)
INPUT – PREGAIN – T1 – VCF – T2 – T3 – EQ – OUTPUT (2)
INPUT – PREGAIN – T1 – T2 – VCF – T3 – EQ – OUTPUT (3)
INPUT – PREGAIN – T1 – T2 – T3 – VCF – EQ – OUTPUT (4)

VCF has 3 options **WIP for the Notch filter that is present on the original**: LP, BP, HP. Depending on where the VCF is insert, you get very different output based on the VCF settings, gain levels, EQ, and output volume. Where it starts to get rather interesting is when you introduce additional insert points, like below with 1 and 3 active:

INPUT – PREGAIN – VCF – T1 – T2 – VCF – T3 – EQ – OUTPUT (1 & 3)

Now the VCF is being affected by the pregain AND the T2 gain at the same time. This sort of routing will net you results like broken tremolo, sputtered filter fuzz, subtle modulation, and more.

Okay, now that you have a very rapid rundown on the PY, here’s the controls and patch explanation.
_________________________________

CONTROL PAGE – module placement is meant to mimic the original

Top row:
VCF REZ (value) – VCF resonance. CW is more.
VCF TYPE (UI/display button) – VCF type. Green=LP, Red=HP, Yellow=BP.
GAIN 4 BIAS (value) – Number of bits for Gain 4/bit crusher. CCW is more bits/dirtier, CW is less bits/cleaner.
VCF FREQ (value) – VCF frequency. Starts at middle freq (880Hz), CW is higher, CCW is lower.

Second row:
I, II, III, IV (pushbuttons) – placement of VCF.

Third row:
LOW CUT (value) – Gain 1/EQ low shelf. CW is boost, CCW is cut.
GAIN 1 (value) – Gain 1/EQ mid gain. CW is boost, CCW is cut
BOOST (stompswitch R) – 6dB boost bypass. LED lit = on, LED dim = off.
FM BEHAVIOR (UI/display button) – FM toggle. Cyan=None, Magenta=inverted, White=non-inverted.

Fourth row:
GAIN 2 (value) – Gain 2 input gain. CW is more.
BASS (value) – EQ low shelf. CW is boost, CCW is cut.
VOLUME (value) – Output volume. CW is more, CW is less.

Bottom row:
GAIN 3 (value) – Gain 3 input gain. CW is more.
TREBLE (value) – EQ high shelf. CW is boost, CCW is cut.
FM (value) – FM multiplier/amount. CW is more, CCW is less.

Left stomp cycles between VCF types. Middle stomp cycles between FM behavior. Right stomp toggles the boost. Audio routing is mono (L) > Stereo Out.

READ ON FOR MORE DETAIL. STOP IF YOU WANNA START PLAYING.
_________________________________

IO PAGE – main routing for dirt
In left, EQ for gain 1, OD (pushed) for both gain 2 and 3, Bit crusher for gain 4, EQ for passive tone, Stereo output with gain control.

VCF PAGE – VCF routing and mixer logic
CV in for VCF frequency. Filter selection via Left stomp and sequencer. Mixer with 4 inputs (each gain stage). Mix level for each is determined by insert points on page 0. Mixer out goes to VCF with 3 outs (lp/bp/hp), sent to audio in switch (channel determined by Left stomp).

FM PAGE – FM logic
Gain 4 output travels to Envelope follower for CV, then into Slew Limiter with separate attack/decay. FM behavior switch takes either 0, slew output inverted, or slew output non-inverted (determined by Middle stomp and sequencer). Switch outputs to multiplier tied to page 0’s FM knob for amount of frequency modulation. Only works if insert point is active.

VCA PAGE – audio routing
4 separate mixers for each gain stage. Channel A’s are the output of gain 1, 2, 3, and 4. Channel B’s are the VCF, with channel selection via insert points on page 0. Outputs to the next gain/EQ along the main routing.
_________________________________

REVISIONS:
1.00: Initial upload.
1.01: Changed bias point on Output gain. If you downloaded this early, change the bias on output gain to -11.18dB (while Volume is set to -1). Added SoundCloud upload as sound demo.
1.02: Fixed mixer issue where II caused excess gain and unwanted feedback when combining with other insert points. Adjusted biasing for Gain 4 control and added expression-via-MIDI (CC 10). Set a better default value for all controls upon patch load. Removed need for DELETE ME module, as v1.09 and above seem to allow for a bit more CPU usage.
1.03: Fixed issue where middle switch triggered the FM toggle CV in switch, causing the filter to temporarily ping between presses (now goes in order from None > Inverted > Non-inverted). Added some volume compensation to the insert points (these route to the Volume value for a bit of boost whenever an insert is added).
1.04: Added a 6dB boost on the right stompswitch (normally on/one). Adjusted the I-IV pushbutton volume compensation amounts. Changed the default values. Removed Cport functionality for both MIDI and CV. Applied starred params to the control page value modules for use with CC’s 1-9 (MIDI channel 1).

