import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42
        self.varasto_mock = Mock()

        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 2:
                return 3
            elif tuote_id == 3:
                return 0

        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            elif tuote_id == 2:
                return Tuote(2,"leipä", 7)
            elif tuote_id == 3:
                return Tuote(3, "juusto", 10)

        self.varasto_mock.saldo.side_effect = varasto_saldo
        self.varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        self.kauppa = Kauppa(self.varasto_mock, self.pankki_mock, self.viitegeneraattori_mock)
        
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called()

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla_1_tuote(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka",42,"12345","33333-44455",5)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla_2_eri_tuotetta_jota_on_tarpeeksi(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka","12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka",42,"12345","33333-44455",12)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla_2_samaa_tuotetta_jota_on_tarpeeksi(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka","12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka",42,"12345","33333-44455",14)

    def test_ostoksen_paatyttya_pankin_metodia_tilisiirto_kutsutaan_oikeilla_parametreilla_2_eri_tuotetta_joista_toista_on_tarpeeksi(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(3)
        self.kauppa.tilimaksu("pekka","12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka",42,"12345","33333-44455",5)

    def test_aloita_asiointi_nollaa_ostokset(self):
        
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka","12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka",42,"12345","33333-44455",7)

    def test_uutta_viitenumeroa_kutsutaan_aina_maksaessa(self):

        viitegeneraattori_mock = Mock(wraps=Viitegeneraattori())
        kauppa = Kauppa(self.varasto_mock,self.pankki_mock,viitegeneraattori_mock)

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka","12345")
        self.assertEqual(viitegeneraattori_mock.uusi.call_count,1)


        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka","12345")
        self.assertEqual(viitegeneraattori_mock.uusi.call_count,2)


        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka","12345")
        self.assertEqual(viitegeneraattori_mock.uusi.call_count,3)

    def test_poista_korista_poistaa_lisatyn_tuotteen(self):

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(2)
        self.kauppa.tilimaksu("pekka","12345")

        self.pankki_mock.tilisiirto.assert_called_with("pekka",42,"12345","33333-44455",5)
