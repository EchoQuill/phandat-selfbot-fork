import base64
exec(base64.b64decode(b'aW1wb3J0IHN5cw0KaW1wb3J0IGpzb24NCmltcG9ydCB0aW1lDQppbXBvcnQgZGF0ZXRpbWUNCmltcG9ydCByZXF1ZXN0cw0KaW1wb3J0IHRocmVhZGluZw0KDQpmcm9tIG93by5jbGllbnQgaW1wb3J0IE93T1NlbGZib3QNCmZyb20ga2FydXRhLmNsaWVudCBpbXBvcnQgS2FydXRhU2VsZmJvdA0KDQpjbGFzcyBLZXlNYW5hZ2VyOg0KCWRlZiBfX2luaXRfXyhzZWxmLCBjbGllbnQpOg0KCQlzZWxmLmNsaWVudCA9IGNsaWVudA0KCQlzZWxmLnBheW1lbnRfa2V5ID0gc2VsZi5nZXRfcGF5bWVudCgpDQoJCXNlbGYudHJpYWxfa2V5ID0gc2VsZi5nZXRfdHJpYWwoKQ0KDQoJZGVmIGdldF9wYXltZW50KHNlbGYpOg0KCQlnaXRodWIgPSByZXF1ZXN0cy5nZXQoc2VsZi5jbGllbnQuZGF0YVsna2V5J11bJ3BheW1lbnQnXSkudGV4dA0KCQlyZXR1cm4gbGlzdChmaWx0ZXIoYm9vbCwgZ2l0aHViLnNwbGl0KCJcbiIpKSkNCg0KCWRlZiBnZXRfdHJpYWwoc2VsZik6DQoJCWdpdGh1YiA9IHJlcXVlc3RzLmdldChzZWxmLmNsaWVudC5kYXRhWydrZXknXVsndHJpYWwnXSkudGV4dA0KCQlyZXR1cm4gbGlzdChmaWx0ZXIoYm9vbCwgZ2l0aHViLnNwbGl0KCJcbiIpKSkNCg0KCWRlZiBnZXRfZGF0ZShzZWxmKToNCgkJZGF0ZSA9IGRhdGV0aW1lLmRhdGV0aW1lLm5vdyhkYXRldGltZS5VVEMpDQoJCXJldHVybiBkYXRlLnllYXIgKiBkYXRlLm1vbnRoICogZGF0ZS5kYXkNCg0KCWRlZiBleHBpcmVfdHJpYWwoc2VsZik6DQoJCWV4cGlyZSA9IGRhdGV0aW1lLmRhdGV0aW1lLm5vdyhkYXRldGltZS5VVEMpLnJlcGxhY2UoaG91ciA9IDAsIG1pbnV0ZSA9IDAsIHNlY29uZCA9IDAsIG1pY3Jvc2Vjb25kID0gMCkNCgkJaWYgZGF0ZXRpbWUuZGF0ZXRpbWUubm93KGRhdGV0aW1lLlVUQykgPCBleHBpcmU6DQoJCQlleHBpcmUgPSBleHBpcmUgLSBkYXRldGltZS50aW1lZGVsdGEoZGF5cyA9IDEpDQoJCWV4cGlyZSA9IChleHBpcmUgLSBkYXRldGltZS5kYXRldGltZS5ub3coZGF0ZXRpbWUuVVRDKSkuc2Vjb25kcw0KCQlwcmludChmIlsrXSBJdCB3aWxsIGV4cGlyZSBpbiB7ZGF0ZXRpbWUudGltZWRlbHRhKHNlY29uZHMgPSBleHBpcmUpfSIpDQoJCXJldHVybihleHBpcmUpDQoNCglkZWYgZW50ZXJfdHJpYWwoc2VsZik6DQoJCWtleSA9IHNlbGYuZ2V0X2RhdGUoKQ0KCQlwcmludChmIlsrXSBHZXQgdHJpYWwga2V5OiB7Jycuam9pbihmJ1xuWytdIHt4fScgZm9yIHggaW4gc2VsZi50cmlhbF9rZXkpfVxuIikNCgkJYW5zd2VyID0gaW5wdXQoIls/XSBFbnRlciB0cmlhbCBrZXk6ICIpDQoJCWlmIGFuc3dlciA9PSBzdHIoa2V5KToNCgkJCXdpdGggb3BlbihzZWxmLmNsaWVudC5maWxlKSBhcyBmaWxlOg0KCQkJCWNvbmZpZyA9IGpzb24ubG9hZChmaWxlKQ0KCQkJY29uZmlnWyd0cmlhbCddID0gYW5zd2VyDQoJCQl3aXRoIG9wZW4oImNvbmZpZ3Mva2V5Lmpzb24iLCAidyIpIGFzIGZpbGU6DQoJCQkJanNvbi5kdW1wKGNvbmZpZywgZmlsZSwgaW5kZW50ID0gNCkNCgkJCXByaW50KGYiWytdIFRoZSB0cmlhbCBrZXkgaXMgQ09SUkVDVCAoe2Fuc3dlcn0pIikNCgkJCXJldHVybiBUcnVlDQoJCWVsc2U6DQoJCQlwcmludChmIlstXSBUaGUgdHJpYWwga2V5IGlzIElOQ09SUkVDVCAoe2Fuc3dlcn0pIikNCg0KY2xhc3MgUGhhbmRhdFNlbGZib3Q6DQoJZGVmIF9faW5pdF9fKHNlbGYpOg0KCQlzZWxmLmZpbGUgPSAiY29uZmlncy9rZXkuanNvbiINCgkJc2VsZi5kYXRhID0gc2VsZi5nZXRfZGF0YSgpDQoJCXNlbGYua2V5X21hbmFnZXIgPSBLZXlNYW5hZ2VyKHNlbGYpDQoNCglkZWYgZ2V0X2RhdGEoc2VsZik6DQoJCXJldHVybiByZXF1ZXN0cy5nZXQoImh0dHBzOi8vcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbS9yZWFscGhhbmRhdC9yZWFscGhhbmRhdC9tYWluL3BoYW5kYXQtc2VsZmJvdC9kYXRhLmpzb24iKS5qc29uKCkNCg0KCWRlZiBvd28oc2VsZik6DQoJCXRocmVhZHMgPSBbXQ0KCQlDbGllbnRzID0gW10NCgkJd2l0aCBvcGVuKCJjb25maWdzL293by5qc29uIikgYXMgZmlsZToNCgkJCWNvbmZpZyA9IGpzb24ubG9hZChmaWxlKQ0KCQlmb3IgdG9rZW4gaW4gY29uZmlnOg0KCQkJQ2xpZW50ID0gT3dPU2VsZmJvdChDbGllbnRzLCB0b2tlbikNCgkJCUNsaWVudHMuYXBwZW5kKENsaWVudCkNCgkJCXRocmVhZCA9IHRocmVhZGluZy5UaHJlYWQodGFyZ2V0ID0gQ2xpZW50LnJ1biwgZGFlbW9uID0gVHJ1ZSwgYXJncyA9ICh0b2tlbiwpKQ0KCQkJdGhyZWFkcy5hcHBlbmQodGhyZWFkKQ0KCQkJdGhyZWFkLnN0YXJ0KCkNCgkJcmV0dXJuIHRocmVhZHMNCg0KCWRlZiBrYXJ1dGEoc2VsZik6DQoJCXRocmVhZHMgPSBbXQ0KCQl3aXRoIG9wZW4oImNvbmZpZ3Mva2FydXRhLmpzb24iKSBhcyBmaWxlOg0KCQkJY29uZmlnID0ganNvbi5sb2FkKGZpbGUpDQoJCWZvciB0b2tlbiBpbiBjb25maWc6DQoJCQlDbGllbnQgPSBLYXJ1dGFTZWxmYm90KHRva2VuKQ0KCQkJdGhyZWFkID0gdGhyZWFkaW5nLlRocmVhZCh0YXJnZXQgPSBDbGllbnQucnVuLCBkYWVtb24gPSBUcnVlLCBhcmdzID0gKHRva2VuLCkpDQoJCQl0aHJlYWRzLmFwcGVuZCh0aHJlYWQpDQoJCQl0aHJlYWQuc3RhcnQoKQ0KCQlyZXR1cm4gdGhyZWFkcw0KDQoJZGVmIHN0YXJ0KHNlbGYpOg0KCQlzZWxmLmNoZWNrX3ZlcnNpb24oKQ0KCQlzZWxmLmNoZWNrX2tleSgpDQoNCglkZWYgcnVuKHNlbGYsIGV4cGlyZSk6DQoJCXRocmVhZHMgPSBbXQ0KCQl3aXRoIG9wZW4oImNvbmZpZ3MvbW9kZS5qc29uIikgYXMgZmlsZToNCgkJCW1vZGUgPSBqc29uLmxvYWQoZmlsZSkNCgkJaWYgbW9kZVsnb3dvJ106DQoJCQl0aHJlYWRzLmV4dGVuZChzZWxmLm93bygpKQ0KCQlpZiBtb2RlWydrYXJ1dGEnXToNCgkJCXRocmVhZHMuZXh0ZW5kKHNlbGYua2FydXRhKCkpDQoNCgkJaWYgZXhwaXJlOg0KCQkJdGltZS5zbGVlcChleHBpcmUpDQoJCQlzeXMuZXhpdCgiWy1dIFRoZSB0cmlhbCBrZXkgZXhwaXJlZCIpDQoJCWVsc2U6DQoJCQlmb3IgdGhyZWFkIGluIHRocmVhZHM6DQoJCQkJdGhyZWFkLmpvaW4oKQ0KDQoJZGVmIGNoZWNrX3ZlcnNpb24oc2VsZik6DQoJCXdpdGggb3BlbigiYXNzZXRzL3ZlcnNpb24udHh0IikgYXMgZmlsZToNCgkJCWN1cnJlbnRfdmVyc2lvbiA9IGZpbGUucmVhZCgpDQoJCWxhc3Rlc3RfdmVyc2lvbiA9IHJlcXVlc3RzLmdldChzZWxmLmRhdGFbJ3ZlcnNpb24nXSkudGV4dA0KCQlpZiBjdXJyZW50X3ZlcnNpb24gPT0gbGFzdGVzdF92ZXJzaW9uOg0KCQkJcHJpbnQoZiJbK10gVGhpcyBpcyB0aGUgbGFzdGVzdCB2ZXJzaW9uICh7bGFzdGVzdF92ZXJzaW9ufSkiKQ0KCQlpZiBjdXJyZW50X3ZlcnNpb24gIT0gbGFzdGVzdF92ZXJzaW9uOg0KCQkJcHJpbnQoZiJbLV0gVGhpcyBpcyB0aGUgb2xkIHZlcnNpb24gKHtjdXJyZW50X3ZlcnNpb259KSIpDQoNCglkZWYgY2hlY2tfa2V5KHNlbGYpOg0KCQlwcmludChyZXF1ZXN0cy5nZXQoc2VsZi5kYXRhWydpbnRybyddKS50ZXh0KQ0KCQlleHBpcmUgPSAwDQoJCXdpdGggb3BlbigiY29uZmlncy9rZXkuanNvbiIpIGFzIGZpbGU6DQoJCQlrZXkgPSBqc29uLmxvYWQoZmlsZSkNCgkJaWYga2V5WydwYXltZW50J10gaW4gc2VsZi5rZXlfbWFuYWdlci5wYXltZW50X2tleToNCgkJCXByaW50KGYiWytdIFRoZSBwYXltZW50IGtleSBpcyBDT1JSRUNUICh7a2V5WydwYXltZW50J119KSIpDQoJCWVsc2U6DQoJCQlwcmludChmIlstXSBUaGUgcGF5bWVudCBrZXkgaXMgSU5DT1JSRUNUICh7a2V5WydwYXltZW50J119KSIpDQoJCQlpZiBrZXlbJ3RyaWFsJ10gPT0gc3RyKHNlbGYua2V5X21hbmFnZXIuZ2V0X2RhdGUoKSk6DQoJCQkJcHJpbnQoZiJbK10gVGhlIHRyaWFsIGtleSBpcyBDT1JSRUNUICh7a2V5Wyd0cmlhbCddfSkiKQ0KCQkJZWxzZToNCgkJCQlpZiBub3Qgc2VsZi5rZXlfbWFuYWdlci5lbnRlcl90cmlhbCgpOg0KCQkJCQlyZXR1cm4NCgkJCWV4cGlyZSA9IHNlbGYua2V5X21hbmFnZXIuZXhwaXJlX3RyaWFsKCkNCgkJc2VsZi5ydW4oZXhwaXJlKQ0KDQppZiBfX25hbWVfXyA9PSAiX19tYWluX18iOg0KCXBoYW5kYXRfc2VsZmJvdCA9IFBoYW5kYXRTZWxmYm90KCkNCglwaGFuZGF0X3NlbGZib3Quc3RhcnQoKQ==').decode("utf-8"))