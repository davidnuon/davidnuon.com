{pkgs ? import <nixpkgs> {}}:
pkgs.stdenv.mkDerivation {
  name = "davidnuon.com-2011";

  src = builtins.path {
    path = ./.;
    name = "davidnuon.com";
  };

  buildInputs = with pkgs; [
    python311
    python311Packages.pyquery
    python311Packages.jinja2
    libxml2
  ];

  buildPhase = ''
    mkdir -p $out
    python generate.py
    cp -r _output/* $out
  '';

  installPhase = ''
    mkdir -p $out
  '';
}
