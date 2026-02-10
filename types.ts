
export enum LubricantType {
  OIL = 'Oil',
  GREASE = 'Grease',
  GLYCOL = 'Glycol',
  CHEMICAL = 'Chemical',
  BARRIER = 'Barrier Fluid',
  COOLANT = 'Coolant'
}

export interface EquipmentData {
  id: string;
  tagNo: string;
  description: string;
  part: string;
  package: string;
  type: LubricantType;
  grade: string;
  initialFill: string;
  topUpQty: string;
  topUpInterval: string;
  replacementInterval: string;
  brands: {
    bp?: string;
    shell?: string;
    mobil?: string;
    total?: string;
    naftal?: string;
    other?: string;
  };
  remarks: string;
}

export type ViewState = 'dashboard' | 'search' | 'ai' | 'details' | 'modified';
