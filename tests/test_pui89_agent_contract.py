import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from pui89_agent_contract import validate_message, validate_evidence, detect_disagreements


def sample(agent='agent-a', value='A'):
    return {'agent_id': agent, 'task_id': 'task-1', 'timestamp': '2026-10-31T08:00:00Z', 'source_ids': ['src-1'], 'observations': [{'kind': 'test'}], 'claims': [{'claim_id': agent + '-1', 'claim_key': 'condition', 'value': value, 'evidence_ids': ['src-1']}], 'confidence': 0.5, 'uncertainty': ['not calibrated'], 'limitations': ['synthetic fixture'], 'status': 'PROPOSED', 'requested_action': 'VERIFY'}

class ContractTests(unittest.TestCase):
    def test_valid_message(self):
        self.assertEqual(validate_message(sample()), [])
    def test_missing_fields_rejected(self):
        self.assertTrue(validate_message({'agent_id': 'x'}))
    def test_unknown_evidence_rejected(self):
        self.assertTrue(any('unknown evidence' in e for e in validate_message(sample(), {})))
    def test_invalid_confidence_rejected(self):
        item = sample(); item['confidence'] = True
        self.assertTrue(any('confidence' in e for e in validate_message(item)))
    def test_evidence_timezone_required(self):
        item = {'source_id':'s','source_type':'image','source_ref':'frame-1','timestamp':'2026-10-31T08:00:00','evidence_kind':'observed','modality':'rgb','lineage':[]}
        self.assertTrue(any('timezone' in e for e in validate_evidence(item)))
    def test_disagreement_is_not_resolved(self):
        found = detect_disagreements([sample('a','left'), sample('b','right')])
        self.assertEqual(found[0]['status'], 'DISAGREEMENT_REQUIRES_REVIEW')
        self.assertIsNone(found[0]['resolution'])

if __name__ == '__main__':
    unittest.main()
